#include "rwLock.h"
#include <iostream>

using namespace std;

void
RWLock::Lock(Mode m)
{
	if (m == RWLock::R) {
		{
			unique_lock<mutex> lock(_mutex);
			_nWReaders++;
			_rCond.wait(lock, [&]{ return _nWWriters == 0 && _nWriters == 0;});
			_nWReaders--;
			_nReaders++;
			return;
		}
	} else {
		{
			unique_lock<mutex> lock(_mutex);
			_nWWriters++;
			_wCond.wait(lock, [&]{ return _nReaders == 0 && _nWriters == 0;});
			_nWWriters--;
			_nWriters++;
		}
	}
}

void RWLock::UnLock(Mode m)
{
	if (m == RWLock::R) {
		{
			unique_lock<mutex> lock(_mutex);
			_nReaders--;
			if (_nReaders == 0) {
				lock.unlock();
				_wCond.notify_all();
			}
		}
	} else {
		{
			unique_lock<mutex> lock(_mutex);
			_nWriters--;
			if (_nWWriters > 0) {
				lock.unlock();
				_wCond.notify_all();
			} else if (_nWReaders > 0) {
				lock.unlock();
				_rCond.notify_all();
			}
		}
	}
}







