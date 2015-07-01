import sys
def Search(string, alphabet):
	invertMap = {}
	for i in range(len(alphabet)):
		invertMap[alphabet[i]] = []
	for i in range(len(string)):
		if string[i] in invertMap:
			invertMap[string[i]].append(i)
	cindexMap = {}
	for key in invertMap:
		cindexMap[key] = 0
	shortest = sys.maxint
	start = -sys.maxint
	end = sys.maxint
	while Condition(invertMap, cindexMap):
		(mi, mikey, ma, makey) = FindMinMax(invertMap, cindexMap)
		shortest = min(shortest, ma - mi)
		if shortest == ma-mi:
			start = mi
			end = ma
		cindexMap[mikey] = cindexMap[mikey] + 1
	return (shortest, start, end)

def Condition(invertMap, cindexMap):
	for key in invertMap:
		if len(invertMap[key]) <= cindexMap[key]:
			return False
	return True
	

def FindMinMax(invertMap, cindexMap):
	mi = sys.maxint
	mikey = None
	ma = -sys.maxint
	makey = None
	for key in invertMap:
		mi = min(invertMap[key][cindexMap[key]], mi)
		if mi == invertMap[key][cindexMap[key]]:
			mikey = key
		ma = max(invertMap[key][cindexMap[key]], ma)
		if ma == invertMap[key][cindexMap[key]]:
			makey = key
	return (mi, mikey, ma, makey)

def main():
	string = "aaccbc"
	alphabet = "abc"
	(shortest, start, end) = Search(string, alphabet)
	print "shortest =", shortest
	print "start =", start
	print "end =", end

if __name__ == "__main__":
	main()
