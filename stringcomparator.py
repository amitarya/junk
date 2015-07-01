def StringCompare(str1, str2):
	i1 = i2 = 0
	while i1 < len(str1) and i2 < len(str2):
		if 48 <= ord(str1[i1]) and ord(str1[i1]) <= 57 and 48 <= ord(str2[i2]) and ord(str2[i2]) <= 57:
			(sum1, i1) = GetNumber(str1, i1)
			(sum2, i2) = GetNumber(str2, i2)
			if sum1 == sum2:
				continue
			elif sum1 < sum2:
					return -1
			else:
				return 1
		else:
			if ord(str1[i1]) == ord(str2[i2]):
				i1 = i1 + 1
				i2 = i2 + 1
				continue
			if ord(str1[i1]) < ord(str2[2]):
				return -1
			else:
				return 1
	if i1 < len(str1):
		return 1
	elif i2 < len(str2):
		return -1
	else:
		return 0


def GetNumber(string, index):
	if index >= len(string):
		return -sys.maxint
	sum1 = 0
	while index < len(string) and 48 <= ord(string[index]) and ord(string[index]) <= 57:
		sum1 = sum1 * 10 + ord(string[index]) - 48
		index = index + 1
	return (sum1, index)
	

def main():
	l = ["a1", "a2", "a11", "a10"]
	for i in range(len(l)):
		for j in range(i, len(l)):
			if StringCompare(l[i], l[j]) == 1:
				temp = l[i]
				l[i] = l[j]
				l[j] = temp
	for i in range(len(l)):
		print l[i]

if __name__ == "__main__":
	main()
