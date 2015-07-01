def atof(string):
	size = len(string)
	dotindex = string.find(".", 0)
	eindex = string.find("e", 0)
	intend = dotindex
	if intend == -1:
		intend = eindex
	if intend == -1:
		intend = size
	integralpart = atoi(string, 0, intend)
	if integralpart == None:
		return None
	frac1start = dotindex
	frac1 = 0
	frac1end = eindex
	if frac1end == -1:
		frac1end = size
	if frac1start != -1:
		frac1 = atoi(string, frac1start+1, frac1end)
		if frac1 != None:
			frac1 = frac1*pow(10, frac1start - frac1end + 1)
			if integralpart < 0:
				frac1 = -frac1
		else:
			return None
	frac2 = 0
	frac2start = eindex
	if frac2start != -1:
		frac2= atoi(string, frac2start + 1, size)
		if frac2 != None:
			frac2 = pow(10, frac2)
		else:
			return None
	return (integralpart + frac1) * frac2

def atoi(string, start, end):
	if end < start:
		return 0
	sign = 1
	index = start
	if string.find("-", start) == start:
		index = index + 1
		sign = -1
	number = 0
	while index < end:
		if 48 <= ord(string[index]) and ord(string[index]) <= 57:
			number = number * 10 + ord(string[index]) - 48
		else:
			return None
		index = index + 1
	return sign * number


def main():
	string = "-1.5e2"
	print atof(string)

if __name__ == "__main__":
	main()


