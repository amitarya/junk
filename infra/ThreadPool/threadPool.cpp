#include "threadPool.h"

using namespace std;


shared_ptr<ThreadPool> ThreadPool::_instance;

/*
 *-------------------------------------------------------------------
 * ThreadPool::Init
 * 	Initialize the ThreadPool object and launch
 * 	as many threads specified by the user.
 *-------------------------------------------------------------------
 */

void ThreadPool::Init(int maxThreads)
{
	_instance.reset(new ThreadPool());
	for (int i = 0;i < maxThreads; i++) {
		shared_ptr<thread> th(new thread(&ThreadPool::Run, _instance));
		_instance->_threads.push_back(th);
	}

}
/*
 *--------------------------------------------------------------------
 * ThreadPool::ScheduleWork
 * 	Put the job in the workQueue and notify the threads waiting on
 * 	workQueue being empty.
 *--------------------------------------------------------------------
 */
void ThreadPool::ScheduleWork(std::function<void(void)> f)
{
	{
		unique_lock<mutex> lock(workQueueMutex);
		workQueue.push(f);
		workQueueEmpty.notify_all();
	}

}

/*
 *--------------------------------------------------------------------
 * ThreadPool::ScheduleWorkAfterTime
 * 	Put the job in the workQueue and notify the threads waiting on
 * 	workQueue being empty.
 *--------------------------------------------------------------------
 */
void ThreadPool::ScheduleWorkAfterTime(std::function<void(void)> f, int time)
{

	ThreadPool::GetInstance()->ScheduleWork([this,f,time](){
		{
			sleep(time);
			unique_lock<mutex> lock(workQueueMutex);
			workQueue.push(f);
			workQueueEmpty.notify_all();
		}});

}


/*
 *---------------------------------------------------------------------
 *
 * ThreadPool::Run
 * 	Pick a job from the workQueue and execute.
 * 	Wait till there is job in the Queue or till
 * 	the use declared that he is finished by invoking
 * 	ThreadPool::Join
 *
 *----------------------------------------------------------------------
 */
void ThreadPool::Run()
{
	std::function<void(void)> f;
	while (true) {
		{
			unique_lock<std::mutex> lock(workQueueMutex);
			workQueueEmpty.wait(lock, [this] {return !workQueue.empty() || finish;});
			/*
			 * I might be woken up when there are no jobs to do. In that case
			 * I should just double confirm that there are no more jobs and
			 * end the thread. Note: "finish" is updated to "true" by the User
			 * who invoked ThreadPool::Join(), thus there is a guarantee if
			 * the workQueue is empty now means all the jobs have been schduled
			 * and its safe for this thread to just finish.
			 */
			if (workQueue.empty()) {
				return;
			}
			f = workQueue.front();
			workQueue.pop();
		}
		f();
	/*
	 * Just for debugging purposes sleep for a second to give other threads
	 * a chance to run the leftover jobs
	 */
	//sleep(1);
	}
}

void ThreadPool::Join()
{
	{
		unique_lock<std::mutex> lock(workQueueMutex);
		/*
		 * We are done scheduling all the work. Update
		 * ThreadPool::finish and notify the threads of that
		 */
		finish = true;
		workQueueEmpty.notify_all();
	}
	for (int i=0; i < _instance->_threads.size(); i++) {
		_threads[i]->join();
	}
}


