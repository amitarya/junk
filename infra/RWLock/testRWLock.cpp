#include "rwLock.h"
#include <iostream>
#include <thread>
#include <vector>


using namespace std;

RWLock rWLock;

void ReadWrite() {
	int n;
	rWLock.Lock(RWLock::R);
	cin >> n;
	rWLock.UnLock(RWLock::R);
	rWLock.Lock(RWLock::W);
	cout << "Thread "<< this_thread::get_id() << " got input " << n << endl;
	rWLock.UnLock(RWLock::W);
}


int main()
{
	vector<thread> v;
	for (int i=0; i<5; i++) {
		v.push_back(thread(&ReadWrite));
	}
	vector<thread>::iterator iter = v.begin();
	for (; iter != v.end();++iter) {
		(*iter).join();
	}
}




