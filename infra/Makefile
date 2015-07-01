CFLAGS= -IThreadPool/ -IRWLock/ --std=c++0x
LDFLAGS= -LThreadPool -LRWLock -lRWLock -lThreadPool -lpthread

test: infra
	LD_LIBRARY_PATH=. ./infra

infra: test.o
	make -C ThreadPool libThreadPool.so
	make -C RWLock libRWLock.so
	cp ThreadPool/lib* .
	cp RWLock/lib* .
	g++ -o $@ $< $(LDFLAGS)

test.o: test.cpp
	g++ -c -o $@ $(CFLAGS) $<

clean:
	rm *.o infra *.so



