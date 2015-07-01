#include <mutex>
#include <condition_variable>
#include <thread>
#include <queue>
#include <functional>
#include <memory>
#include <vector>
#include <unistd.h>

class ThreadPool {
	public:
	static void Init(int maxNumberOfThreads);
	void ScheduleWork(std::function<void(void)> f);
	void ScheduleWorkAfterTime(std::function<void(void)> f, int time);
	static ThreadPool* GetInstance() {
		return _instance.get();
	}
	void Join();
	private:
		void Run();
		ThreadPool() : finish(false) {}
		static std::shared_ptr<ThreadPool> _instance;
		std::queue<std::function<void(void)> > workQueue;
		std::mutex workQueueMutex;
		std::condition_variable workQueueEmpty;
		bool finish;
		std::vector<std::shared_ptr<std::thread> > _threads;
};
