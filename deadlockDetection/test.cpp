#include <iostream>
#include <thread>
#include <mutex>
bool global1;
bool global2;

using namespace std;

class MutexLocker : public mutex {
	public:
	MutexLocker(mutex &m): _mutex(m){ _mutex.lock(); }
	~MutexLocker() { _mutex.unlock(); };

	private:
	mutex &_mutex;
};
mutex changeGlobal1;
mutex changeGlobal2;

void ChangeGlobalOrder1() {
	MutexLocker lock1(changeGlobal1);
	global1 = !global1;
	sleep(5);
	MutexLocker lock2(changeGlobal2);
	global2 = !global2;
}

void ChangeGlobalOrder2() {
	MutexLocker lock2(changeGlobal2);
	global2 = !global2;
	sleep(5);
	MutexLocker lock1(changeGlobal1);
	global1 = !global1;
}
int main(int argc, char *argv[]) {
	thread t1(ChangeGlobalOrder1);
	thread t2(ChangeGlobalOrder2);
	t1.join();
	t2.join();
}
