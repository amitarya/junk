def NNGridPath(i, j, N, dp):
	if i >= N:
		return 0
	if j >= N:
		return 0
	if i == N-2 and j==N-1:
		return 1
	if i == N-1 and j==N-2:
		return 1
	if dp[i][j] != None:
		return dp[i][j]
	dp[i][j] = NNGridPath(i+1, j, N, dp) + NNGridPath(i, j+1, N, dp)
	return dp[i][j]

def main():
	a = 4
	print NNGridPath(0,0, a, [[None for x in range(a)]for x in range(a)])

if __name__ == "__main__":
	main()




