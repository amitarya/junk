/*
 * This Programme computes the starting number which
 * produces the longest Collatz sequence.
 */

#include <iostream>
#include <cstring>
#include <ctime>

using namespace std;

#define MAX_START_NUM 1000000

unsigned long SeqLengthsCache[MAX_START_NUM];

unsigned long
FindCollatzSeqLen(const unsigned long start)
{
	const unsigned long cacheIndex = start - 1;
	if (SeqLengthsCache[cacheIndex] > 0) {
		return SeqLengthsCache[cacheIndex];
	}
	unsigned long result = 0;
	unsigned long current = start;
	while (current > 1) {
		/*
		 * If current is already in the cache then we don't need to
		 * iterator further as we can reuse the cached value.
		 */
		if (current <= MAX_START_NUM && SeqLengthsCache[current-1] > 0) {
			break;
		}
		result++;
		current = (current & 1) == 0? current >> 1 : current * 3 + 1;
	}
	SeqLengthsCache[cacheIndex] = result + SeqLengthsCache[current-1];
	return SeqLengthsCache[cacheIndex];
}

unsigned long
FindLongestStart()
{
	memset(SeqLengthsCache, 0, MAX_START_NUM * sizeof(unsigned long));
	unsigned long maxLen = 0;
	unsigned long result = 0;
	for (unsigned long i = 2; i < MAX_START_NUM; i++) {
		unsigned long len = FindCollatzSeqLen(i);
		if (maxLen < len) {
			maxLen = len;
			result = i;
		}
	}
	return result;
}


int main() {
	const clock_t beginTime = clock();
	cout << FindLongestStart() << endl;
	cout << "Time taken = "<< float(clock() - beginTime)/CLOCKS_PER_SEC << endl;
}
