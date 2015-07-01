import sys, random
def MaxProduct(a):
	maxi = FindKth(a, len(a) - 1)
	print maxi
	maxi2 = FindKth(a, len(a) - 2)
	maxi3 = FindKth(a, len(a) - 3)
	prod = maxipos * maxi2pos * maxi3pos
	mini = FindKth(a, 0)
	mini2 = FindKth(a, 1)
	prod2 = maxi * mini * mini2
	if prod > prod2:
		return prod
	return prod2
	



def FindKth(a, k):
	if k == 0 and len(a) == 1:
		return a[0]
	if k == 0 and len(a) == 2:
		return min(a)
	if k == 1 and len(a) == 2:
		return max(a)
	pivot = random.randint(0, len(a) - 1)
	swap(a, 0, pivot)
	i = 0
	for j in range(1, len(a)):
		if a[j] <= a[i] and j-i > 1:
			swap(a,i+1, j)
			i = i+1
	if i == k:
		return a[i]
	elif i < k:
		return FindKth(a[i+1:], k-i-1)
	else:
		return FindKth(a[1:i-1], k)

def swap(a, i, j):
	a[i] = a[i] ^ a[j]
	a[j] = a[i] ^ a[j]
	a[i] = a[i] ^ a[j]




def main():
	a = [1,3,5,2,8,0,-1,3]
	print a
	swap(a,3,4)
	print a
	MaxProduct(a)

if __name__ == "__main__":
	main()
