import sys
def FindMinNumber(i, x, s):
	if s[i][x] != -1:
		return s[i][x]
	if i == 1:
		return 1
	if x == 1:
		return i
	if x == 0:
		return sys.maxint
	if i == 0:
		return 0
	result = sys.maxint
	for j in range(1, i+1):
		result = min(result, max(FindMinNumber(j-1, x-1, s),
					FindMinNumber(i-j, x,
				s)))
	s[i][x] = result + 1
	return s[i][x]



def main():
	n = 100
	k = 4
	s = [[-1 for x in range(k+1)] for x in range(n+1)]
	print FindMinNumber(n,k,s)


if __name__ == "__main__":
	main()
