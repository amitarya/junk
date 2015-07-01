def mod(n):
	if n > 0:
		return n
	else:
		return -n

def check(i, queens):
	for j in range(i):
		if queens[i] == queens[j]:
			return False
		if mod(queens[i]-queens[j]) == mod(i-j):
			return False
	
	return True

def NQueen(queens, row = 0, N=8):
	if row == N:
		return True
	for i in range(N):
		queens[row] = i
		if check(row, queens):
			if NQueen(queens, row + 1, N):
				return True
	return False

def main():
	queens = {}
	NQueen(queens)
	for i in range(8):
		for j in range(8):
				if queens[i]==j:
					print "X",
				else:
					print "-",
		print
	print queens

if __name__ == "__main__":
	main()

