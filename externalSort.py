import sys, array, heapq, tempfile

def ReadFromFile(tFile):
	while True:
		a = array.array('i')
		a.fromstring(tFile.read(4000))
		if not a:
			break
		for value in a:
			yield value

def SortedPartitions(sArrays):
	while True:
		a = array.array('i')
		a.fromstring(sys.stdin.read(40000))
		if not a:
			break
		tempFile = tempfile.TemporaryFile()
		array.array('i', sorted(a)).tofile(tempFile)
		tempFile.seek(0)
		sArrays.append(ReadFromFile(tempFile))

def ExternalSort():
	sArrays = []
	SortedPartitions(sArrays)
	a = array.array('i')
	for value in heapq.merge(*sArrays):
		a.append(value)
		if len(a) > 1000:
			a.tofile(sys.stdout)
			del a[:]
	if a:
		a.tofile(sys.stdout)

def main():
	ExternalSort()

if __name__ == "__main__":
	main()

