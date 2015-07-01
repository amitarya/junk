import random
def FindMedian(arr):
	n = len(arr)
	if n%2 == 0:
		return (float(FindKth(arr, n/2 -1)) + float(FindKth(arr, n/2)))/2
	else:
		return FindKth(arr, (n+1)/2 -1)

def FindMedianSorted(a):
	n = len(arr)
	if n%2 == 0:
		return (float(a[n/2-1])+a[n/2])/2
	else:
		return a[(n+1)/2 - 1]

def FindDistMedian(larr):
	l = {}
	medarr = []
	for i in larr:
		med = FindMedianSorted(i)
		l[i] = med
		medarr.apend(med)
	medarrmed = FindMedian(medarr)
	for u in l:
		if l[u] < medarrmed
			l[u] = l[u][n/2:]
		else:
			l[u] = l[u][0, n
		
	
	
def FindKth(arr, k):
	if k < 0 or k >= len(arr):
		return -1
	if k == 0 and len(arr) == 1:
		return arr[0]
	pivot = random.randint(0, len(arr) -1)
	i = 0
	swap(arr, 0, pivot)
	for j in range(1,len(arr)):
		if arr[j] < arr[0]:
			i = i + 1
			swap(arr, i, j)
	swap(arr, 0, i)
	if i < k:
		return FindKth(arr[i+1:len(arr)], k - i -1)
	elif i == k:
		return arr[i]
	else:
		return FindKth(arr[0:i], k)


def swap(a, i, j):
	temp = a[i]
	a[i] = a[j]
	a[j] = temp
	
def main():
	a = [random.randint(1,10) for i in range(10)]
	print FindKth(a, 4)
	print FindMedian(a)
	a.sort()
	print a

if __name__ == "__main__":
	main()
