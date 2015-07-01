def GreatestNSmallerthanNumber(n):
	temp = n
	digit = 0
	s = 0
	prev = None
	while temp>0:
		currentdigit = temp%10
		if prev != None and currentdigit > prev:
			(digitMax, digitMaxI) = MaxDigitLessThanCurr(s, currentdigit)
			s = s + (currentdigit - digitMax) * pow(10,digitMaxI)
			s = s + digitMax * pow(10, digit)
			s = s +  (temp/10) * pow(10, digit + 1)
			return s
		else:
			s = s + (currentdigit) * pow(10, digit)
		prev = currentdigit
		temp = temp/10
		digit = digit + 1
	return s

def AllNumbersLessThanN(n):
	temp = n
	digits = []
	while temp>0:
		digits.append(temp%10)
		temp = temp/10
	Permutations(digits, n)

def Permutations(digits, n):
	PermutationsInt(digits, n)

def PermutationsInt(digits, n, index=0):
	if index == len(digits):
		num = ConvertToNumber(digits)
		if num < n:
			print num
	for i in range(index, len(digits)):
		swap(digits, index, i)
		PermutationsInt(digits,n, index+1)
		swap(digits, index, i)

def ConvertToNumber(digits):
	num = 0
	for i in range(len(digits)):
		num = num + digits[i]*pow(10,i)
	return num
def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp

def MaxDigitLessThanCurr(n, curr):
	temp = n
	digitI = 0
	maxDigitI = 0
	maxDigit = 0
	while temp > 0:
		c = temp%10
		if c > maxDigit and c < curr:
			maxDigitI = digitI
			maxDigit = c
		temp = temp/10
		digitI = digitI + 1
	return (maxDigit, maxDigitI)


def SwapDigits(n, i, j):
	digitI = -1
	digitJ = -1
	digit = 0
	temp = n
	while temp > 0:
		if digit == i:
			digitI = temp%10 
		if digit == j:
			digitJ = temp%10
		temp = temp/10
		digit = digit +1 
	if digitI >= 0 and digitJ >=0 and digitI != digitJ:
		n = n + (digitI - digitJ) * pow(10, j) + (digitJ-digitI) * pow(10, i)
	return n


def IterOverDigitsWithoutChangingTheNumber(n):
	temp = n
	digit = 0
	s = 0
	while temp>0:
		s = s + (temp%10) * pow(10, digit)
		temp = temp/10
		digit = digit + 1
	return s
def main():
	print IterOverDigitsWithoutChangingTheNumber(618)
	print GreatestNSmallerthanNumber(685769)
	print SwapDigits(12345, 1, 3)
	AllNumbersLessThanN(685769)
if __name__ == "__main__":
	main()
