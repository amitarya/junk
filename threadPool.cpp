#include "threadPool.h"
#include <iostream>

using namespace std;


shared_ptr<ThreadPool> ThreadPool::_instance;

void testFunction(int);
void ThreadPool::Init(int maxThreads)
{
	_instance.reset(new ThreadPool());
	for (int i = 0;i < maxThreads; i++) {
		shared_ptr<thread> th(new thread(&ThreadPool::Run, _instance));
		_instance->_threads.push_back(th);
	}

}

void ThreadPool::ScheduleWork(std::function<void(void)> f)
{
	{
		unique_lock<mutex> lock(workQueueMutex);
		workQueue.push(f);
		workQueueEmpty.notify_all();
	}

}


void ThreadPool::Run()
{
	std::function<void(void)> f;
	while (true) {
	{
		unique_lock<std::mutex> lock(workQueueMutex);
		workQueueEmpty.wait(lock, [this] {return !workQueue.empty() || finish;});
		if (workQueue.empty()) {
			return;
		}
		cout << " thread id waiting--> " << this_thread::get_id() << endl;
		f = workQueue.front();
		workQueue.pop();
	}
	f();
	/*
	 * Just for debugging purposes sleep for a second to give other threads
	 * a chance to run the leftover jobs
	 */
	sleep(1);
	}
}

void ThreadPool::Join()
{
	{
		unique_lock<std::mutex> lock(workQueueMutex);
		finish = true;
		workQueueEmpty.notify_all();
	}
	for (int i=0; i < _instance->_threads.size(); i++) {
		_threads[i]->join();
	}
}
// Testing

void testFunction(int a) {
		cout << "Job " << a << " was done by thread with id --> "  << this_thread::get_id() << endl;
}

int main() {
	ThreadPool::Init(5);
	for (int i =0;i < 50;i++) {
		function<void(int)> f = testFunction;
		ThreadPool::GetInstance()->ScheduleWork(std::bind(f, i));
	}
	ThreadPool::GetInstance()->Join();

}

