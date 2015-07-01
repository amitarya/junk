import random
import sys

class Interval:
	def __init__(self,left, right):
		self.left = left
		self.right = right

def FindIfMerge(i1, i2):
	if i1.left < i2.left and i2.left < i1.right:
		return True
	if i2.left < i1.left and i1.left < i2.right:
		return True
	return False

def Merge(i1, i2):
	if FindIfMerge(i1, i2):
		if i1.left < i2.left:
			return Interval(i1.left, max(i2.right, i1.right))
		else:
			return Interval(i2.left, max(i1.right, i2.right))
	
	return Interval(0,0)

def Print(i):
	print "[",i.left ,",",i.right,"]"
	
def Compare(i1, i2):
	if i1.left <= i2.left:
		return True
	else:
		return False


def Sort(l, start, end):
	if start >= end:
		return
	p = random.randint(start, end)
	pIndex = start-1
	for i in range(start, end+1):
		if Compare(l[i],l[p]):
			pIndex = pIndex + 1
			temp = l[pIndex]
			l[pIndex] = l[i]
			l[i] = temp
	Sort(l, start, pIndex)
	Sort(l, pIndex+1, end)
	

def MergeAndSort(l):
	Sort(l, 0, len(l) - 1)
	end = l[0].right
	result = [l[0]]
	count = 0
	for i in range(1, len(l)):
		if l[i].left < end:
			result[count] = Merge(result[count], l[i])
			print "merge"
			end = max(end, l[i].right)
		else:
			result.append(l[i])
			count = count + 1
			end = l[i].right
	return result

def main():
	i1 = Interval(3,5)
	i2 = Interval(2,8)
	i4 = Interval(9, 10)
	i5 = Interval(1, 6)
	i6 = Interval(11, 12)
	i7 = Interval(0, 5)
	l = [i1, i2, i4, i5, i6, i7]
	Sort(l,0 , len(l) - 1)

	#print FindIfMerge(i1, i2)
	i3 = Merge(i1, i2)
	res = MergeAndSort(l)
	for i in range(len(l)):
		Print(l[i])
	print "After"
	for i in range(len(res)):
		Print(res[i])
	

if __name__ == "__main__":
	main()
