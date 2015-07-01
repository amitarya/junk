#! /usr/bin/env python
import struct
import string
def ncr(str, i , r, picked=[], rmap=dict([])):
	if len(picked) == r:
		comb = ''.join(picked)
		if comb in rmap:
			print "subsequence repeated --> %s"%comb
			return True
		else:
			rmap[comb] = 1
			return False
	for j in range(i, len(str)):
		picked.append(str[j])
		if (ncr(str, j+1, r, picked)) == True:
			return True
		else:
			picked.pop()

def main():
	st = "ABCBE"
	ncr(st, 0, 3)
	n = 10
	r = 4
	sum1 = 0
	dp = [[-1 for x in range(n+1)] for x in range(r)]
	for i in range(1,n+1):
		sum1 = sum1+ DP(r,i,dp)
	print sum1
	prod = 1
	for k in range(r):
		prod = prod * (n+k)/(k+1)
	print prod
def DP(r, i, dp):
	if r==1:
		return 1
	sum1 = 0
	for j in range(1,i+1):
		if dp[r-1][j] == -1:
			dp[r-1][j] = DP(r-1, j, dp)
		sum1 = sum1 + dp[r-1][j]
	return sum1

if __name__ == "__main__":
	main()

