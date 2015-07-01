/*
 * This is to test the threadPool library. We will check if each thread
 * gets a fair chance. From the output we see each job is run by which
 * We spawn 50 jobs and see if all the threads did a fair share. Note
 * This is just for the testing purpose as we have put a sleep in the
 * ThreadPool::Run method. In reality threads may not get a fair share.
 */

#include "threadPool.h"
#include <iostream>
#include <map>


using namespace std;
mutex coutMutex;
mutex threadJobsCountMutex;
map<thread::id, int> threadJobsCount;
const int NJobs = 10;
const int NThreads = 10;
const std::string currentDateTime() {
	time_t     now = time(0);
	struct tm  tstruct;
	char       buf[80];
	tstruct = *localtime(&now);
	// Visit
	// http://en.cppreference.com/w/cpp/chrono/c/strftime
	// for more information about date/time format
	strftime(buf, sizeof(buf), "%Y-%m-%d.%X", &tstruct);

	return buf;
}
void testFunction(int a) {
	{ 
		lock_guard<mutex> lock(threadJobsCountMutex);
		threadJobsCount[this_thread::get_id()]++;
	}
	{
		lock_guard<mutex> lock(coutMutex);
		cout << "Job " << a << " was done by thread with id --> "  <<
			this_thread::get_id() << " at "<< currentDateTime() << endl;
	}
}

int main() {
	ThreadPool::Init(NThreads);
	for (int i =0;i < NJobs;i++) {
		function<void(int)> f = testFunction;
		cout << "Job " << i << " was scheduled at "<< currentDateTime() << " to "
			"run after "<< i << " seconds"<<endl;
		ThreadPool::GetInstance()->ScheduleWorkAfterTime(std::bind(f, i), i);
	}
	ThreadPool::GetInstance()->Join();
	// Test the count of each thread
	map<thread::id, int>::const_iterator iter = threadJobsCount.begin();
	for ( ;iter != threadJobsCount.end(); ++iter) {
		cout << "Thread with id(" << iter->first << ") did " << iter->second <<
			" Jobs" << endl;
	}
}
