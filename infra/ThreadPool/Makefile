test: testLauncher
	LD_LIBRARY_PATH=. ./testLauncher

all: testLauncher

testLauncher: threadPoolTest.cpp libThreadPool.so
	g++ -std=c++0x threadPoolTest.cpp -o $@ -L. -lThreadPool -lpthread

libThreadPool.so: threadPool.cpp threadPool.h
	g++ -c -std=c++0x -fPIC threadPool.cpp -o threadPool.o
	g++ -shared -o $@ threadPool.o
	rm threadPool.o

clean: testLauncher libThreadPool.so
	rm testLauncher libThreadPool.so
