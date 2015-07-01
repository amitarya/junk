import heapq, sys
def createdinvertedMap(word):
	result = {}
	i = 0
	for w in word:
		if w not in result:
			result[w] = [i]
		else:
			result[w].append(i)
		i = i + 1
	return result

def findShortestSniplet(m, word, alphabets):
	size = len(m)
	if len(m) < len(alphabets):
		return (-1, -1)
	minh = []
	maxh = []
	for w in m:
		i = iter(m[w])
		val = next(i, sys.maxint)
		heapq.heappush(minh, (val, i))
		heapq.heappush(maxh, -val)
	mind = sys.maxint
	start = 0
	end = 0
	minval = maxval = 0
	while minval != sys.maxint and maxval != sys.maxint:
		(minval, it1) = minh[0]
		maxval = -maxh[0]
		print minval, maxval
		if minval != sys.maxint and maxval != sys.maxint and mind > maxval - minval:
			mind = maxval - minval
			start = minval
			end = maxval
		val = next(it1, sys.maxint)
		heapq.heapreplace(minh, (val, it1))
		heapq.heappush(maxh, -val)
	print start, end
	return (start, end)

	
def main():
	word = "aacaybcmi"
	alphabets = "abcmiy"
	m = createdinvertedMap(word)
	for i in m:
		print i, "-->",
		for v in m[i]:
			print v,
		print
	(start, end) = findShortestSniplet(m, word, alphabets)
	for i in range(start, end+1):
		print word[i],
	print


if __name__ == "__main__":
	main()



	
	
