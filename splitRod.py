import random
price = [0,2,5,9,9]
def splitRod(n, dp):
	if n==1:
		dp[1] = price[1]
		return dp[1]
	if dp[n] == -1:
		for i in range(1,n):
			dp[n] = max(dp[n], max(splitRod(n-i, dp) + splitRod(i, dp),
				price[n]))
	return dp[n]


def main():
	n = 4
	dp = [-1 for x in range(n+1)]
	#price = [0, 2, 5, 3, 9]
	#for i in range(1,n+1):
	#	p = random.randint(1,n)
	#	price.append(p)
	print "price -->",price
	print splitRod(n, dp)
	print dp	

if __name__ == "__main__":
	main()
