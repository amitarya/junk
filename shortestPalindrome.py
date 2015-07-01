#!/usr/bin/env python

s = []
def shortestPalindrome(string, i):
	# flag 1 ---> include left
	# flag 2 --> include right
	# flag 3 --> exclude
	if s[i] < 90:
		return s[i]
	s[i] = min(min(GiveShortestEditIfPossible(string, i, i+1),
		GiveShortestEditIfPossible(string, i-1,i)),
		GiveShortestEditIfPossible(string, i-1, i+1))
	return s[i]

def GiveShortestEditIfPossible(string, i, j):
	if i == -1 or j == len(string):
		return len(string)
	a = i
	b = j
	while string[a]==string[b]:
		a = a -1
		b = b + 1
		if a < 0:
			return len(string) - b
		if b > len(string) - 1:
			return a+1
	return 90
	
def SP(string, l, r):
	index = 0
	for i in range(len(string)):
		if h(string,i,l,r) == 1:
			if index < i:
				index = i
	pal = len(string) - 1 - index
	st = string[::-1]
	print pal
	index = 0
	for i in range(len(st)):
		if h(st,i,l,r) == 1:
			if index < i:
				index = i
	pal = max( pal, len(st) - 1 - index)
	return len(string) - pal


		
def h(string, i, l, r):
	if i == 0:
		l[i] = 0
		r[i] = 0
	if i % 2 == 0:
		l[i] = l[i-1]
		r[i] = r[i-1] - ord(string[int(i/2)]) * pow(101, int(i/2) - 1) + ord(string[i])
	else:
		l[i] = l[i-1] + ord(string[int((i-1)/2)]) * pow(101, int((i-1)/2))
		r[i] = r[i-1]*101 + ord(string[i])
	if l[i]==r[i]:
		return 1
	else:
		return 0

def dp(DP,string, i, S):
	if DP[i] != sys.maxint:
		return dp[i]
	if i == 0 or i == len(string) -1:
		return 1
	DP[i][S] = 0
		

def isAPalindrome(string):
	i = 0
	j = len(string) -1
	if i==j:
		return 1
	#while (i<j)
	
def fix(a):
	partition(a)
	print a
	count = 0
	for i in range(len(a)):
		if a[i] < 0:
			count = count + 1
		else:
			break
	if count == 1 or count == 0:
		return
	i = 1
	j = count
	while i <= count:
		swap(a,i,i+1)
		swap(a,i,j)
		i= i+2
		j=j+1


def partition(a):
	j=-1
	i=0
	l = len(a)-1
	k = len(a)
	while i < len(a)-1:
		if a[i] < 0:
			j = j+1
			swap(a,i,j)
		if a[l] >= 0:
			k = k-1
			swap(a,l,k)
		print a
		i = i+1
		l = l-1
	
def swap(a,i,j):
	temp = a[i]
	a[i]=a[j]
	a[j]=temp
	

def findmaxInversions(DP,a,i,j):
	if i>=j:
		return -1
	if i==j-1:
		if a[i]> a[j]:
			return 1
		else:
			return -1
	if DP[i][j] != -1:
		return DP[i][j]
	if a[i]>a[j]:
		return j-i
	DP[i][j]= max(findmaxInversions(DP,a,i+1,j),findmaxInversions(DP,a,i,j-1))
	return DP[i][j]

def FMInversions(a,i,j):
	if i>=j:
		return -1
	if i==j-1:
		if a[i]>a[j]:
			return 1
		else:
			return -1
	maxi = FMInversions(a,i,(i+j)/2)
	maxi = max(maxi,FMInversions(a,(i+j)/2+1,j))
	start1=i
	start2=(i+j)/2+1
	while start2<=j:
		while start1<=(i+j)/2:
			if a[start1] > a[start2]:
				maxi = max(maxi, start2-start1)
			start1= start1+1
		start2 = start2+1
	return maxi
		
def CInversions(a,i,j):
	count = 0
	if i>=j:
		return count
	if i==j-1:
		if a[i]>a[j]:
			swap(a,i,j)
			count=count+1
		return count
	mid = (i+j)/2
	count = count + CInversions(a,i,mid)
	count = count + CInversions(a,mid+1,j)
	scartch = []
	start1 = i
	start2 = mid+1
	while start1<=mid and start2<=j:
		if a[start2]<a[start1]:
			scartch.append(a[start2])
			start2 = start2 + 1
			count = count + mid - start1+1
		else:
			scartch.append(a[start1])
			start1 = start1 + 1
	while start1<=mid:
		scartch.append(a[start1])
		start1 = start1+1
	while start2<j:
		scartch.append(a[start2])
		start2= start2 + 1
	print scartch	
	for loop in range(len(scartch)):
		a[loop+i]=scartch[loop]
	return count

	
def main():
	string = "brara"
	minlen = 90
	index = -1
	for i in range(len(string)):
		s.append(90)
		tempmin = minlen
		minlen = min(minlen, shortestPalindrome(string, i))
		if tempmin > minlen:
			index = i
	l = [0 for x in range(len(string))]
	r = [0 for x in range(len(string))]
	print "SP = %s" % SP(string, l, r)

	return (minlen, index)

if __name__ == "__main__":
	print main()
	a = [1,5,3,2,7,4]
	print a
	DP = [[-1 for x in range(len(a))] for y in range(len(a))]
	print findmaxInversions(DP,a,0,len(a)-1)
	print FMInversions(a,0,len(a)-1)
	print CInversions(a,0,len(a)-1)
	print a
	fix(a)
	print a
