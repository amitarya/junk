#include <mutex>
#include <condition_variable>

class RWLock {
	private:
		std::mutex _mutex;
		int _nReaders;
		int _nWWriters;
		int _nWReaders;
		int _nWriters;
		std::condition_variable _wCond;
		std::condition_variable _rCond;
	public:
		enum Mode {
			R,
			W
		};
		RWLock() :
			_mutex(), _nReaders(0), _nWWriters(0),
			_nWriters(0), _nWReaders(0)
	   {
		}
		void Lock(Mode m);
		void UnLock(Mode m);
};
