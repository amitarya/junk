CXX=g++ -ggdb
DEBUG?=0
GDB=
ifeq ($(DEBUG),1)
	GDB=gdb
endif
test: testLauncher
	LD_LIBRARY_PATH=. $(GDB) ./testLauncher

all: testLauncher

testLauncher: testRWLock.cpp libRWLock.so
	$(CXX) -std=c++0x testRWLock.cpp -o $@ -L. -lRWLock -lpthread

libRWLock.so: rwLock.cpp rwLock.h
	$(CXX) -c -std=c++0x -fPIC rwLock.cpp -o rwLock.o
	$(CXX) -shared -o $@ rwLock.o
	rm rwLock.o

clean: testLauncher libRWLock.so
	rm testLauncher libRWLock.so


