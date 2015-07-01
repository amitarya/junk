def If3NumberMatchToSum(a):
	a.sort()
	for i in range(len(a)):
		j = i+1
		k = len(a) - 1
		while k > j:
			temp = a[i]+a[j]+a[k]
			if temp == 0:
				print (a[i],a[j],a[k])
				return True
			elif temp > 0:
				k = k -1
			else:
				j = j+1

def main():
	a = [1,4,-1, 0, 5,-5]
	print If3NumberMatchToSum(a)

if __name__ == "__main__":
	main()


