def FindSubstring(string, sub):
	hashSub = ComputeHash(sub, 0 , len(sub))
	print hashSub
	hashFrame = ComputeHash(string, 0, len(sub))
	if hashFrame == hashSub:
		return 0
	print hashFrame
	for i in range(1,len(string)-len(sub)):
		hashFrame = ComputeHash(string, i, len(sub), hashFrame)
		print hashFrame
		if hashFrame == hashSub:
			return i
	return -1
	


def ComputeHash(string, index, l, prev = None):
	if prev != None and index > 0:
		pChar = string[index -1]
		return prev * 101 - ord(pChar) * pow(101,l) + ord(string[index+l-1])
	else:
		count = l-1
		sum = 0
		print string, index, l
		limit = index + l
		while index < limit:
			sum = sum + pow(101, count) * ord(string[index])
			count = count - 1
			index = index + 1
		return sum


def main():
	string = "AMITARYA"
	sub = "ITA"
	print FindSubstring(string, sub)

if __name__ == "__main__":
	main()

