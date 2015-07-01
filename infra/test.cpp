#include <threadPool.h>
#include <rwLock.h>
#include <vector>
#include <cstdlib>
#include <iostream>

using namespace std;

const int NUM_READERS = 50;
const int NUM_WRITERS = 5;
const int NUM_THREADS = 32;

vector<int> globalVector = {0,1,2};
RWLock locker;

void 
Read()
{
	locker.Lock(RWLock::R);
	int index = rand() % globalVector.size();
	cout << "Reading random index " << index << " value = " <<
		globalVector[index] << endl;
	locker.UnLock(RWLock::R);
}

void 
Write()
{
	locker.Lock(RWLock::W);
	int index = globalVector.size();
	cout << "Writing index " << index << " value = " <<
		index << endl;
	globalVector.push_back(index);
	locker.UnLock(RWLock::W);
}

int main() {
	ThreadPool::Init(NUM_THREADS);
	int readers = 0, writers = 0;
	while (readers < NUM_READERS && writers < NUM_WRITERS) {
		ThreadPool::GetInstance()->ScheduleWork(&Read);
		readers++;
		ThreadPool::GetInstance()->ScheduleWork(&Write);
		writers++;
	}
	while (readers < NUM_READERS) {
		ThreadPool::GetInstance()->ScheduleWork(&Read);
		readers++;
	}
	ThreadPool::GetInstance()->Join();
}

