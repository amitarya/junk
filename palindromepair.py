def findPalindrome(dictionary):
	for x in dictionary:
		for y in dictionary:
			if x == y:
				continue
			if x+y == reverse(x+y):
				yield (x,y)
			if y+x == reverse(y+x):
				yield (y,x)


def reverse(x):
	result = ""
	j = len(x) - 1
	while j > -1:
		result = result+x[j]
		j = j-1
	return result

def main():
	dictionary = set(['cigar', 'tragic','none', 'xenon', 'warrener', 'raw',
	'rotatively', 'levitator', 'redrawer', 'rewarder'])
	seenmap = {}
	for (first,second) in findPalindrome(dictionary):
		if first not in seenmap:
			seenmap[first] = set([second])
			print (first, second)
		else:
			if second not in seenmap[first]:
				seenmap[first].add(second)
				print (first, second)
	
if __name__ == "__main__":
	main()

