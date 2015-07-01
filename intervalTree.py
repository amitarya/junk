#! /usr/bin/env python

import sys
class IT:
	def __init__(self, intervals , arr):
		L = []
		R = []
		M = []
		medIndex = (len(arr))/2
		median = arr[medIndex]
		for loop in range(len(intervals)):
			if intervals[loop][0] <= median and median <= intervals[loop][1]:
				M.append(intervals[loop])
			elif median < intervals[loop][0]:
				R.append(intervals[loop])
			else:
				L.append(intervals[loop])
		self.key = median
		self.left = None
		self.right = None
		self.intervals = M
		if len(L) > 0:
			self.left = IT.FromIntervals(L)
		if len(R) > 0:
			self.right = IT.FromIntervals(R)

	@classmethod
	def FromIntervals(cls, intervals):
		x = []
		for i in range(len(intervals)):
			x.append(intervals[i][0])
			x.append(intervals[i][1])
		x.sort()
		return cls(intervals, x)

	@staticmethod
	def Query(tree, k):
		if tree == None:
			return []
		result = []
		for i in range(len(tree.intervals)):
			if tree.intervals[i][0] <= k and k <= tree.intervals[i][1]:
				result.append(tree.intervals[i])
		if k < tree.key:
			result = result + IT.Query(tree.left, k)
		elif k > tree.key:
			result = result + IT.Query(tree.right, k)
		return result

	@staticmethod
	def AllConflictingIntervals(tree):
		x = []
		for i in range(len(tree.intervals)):
			x.append(tree.intervals[i][0])
			x.append(tree.intervals[i][1])
		print "Conflicting Intervals Begin"
		for i in range(len(x)):
			print IT.Query(tree,x[i])
		print "Conflicting Intervals End"


	@staticmethod
	def FindNumInMaxIntervals(root):
		x = []
		for i in range(len(root.intervals)):
			x.append(root.intervals[i][0])
			x.append(root.intervals[i][1])
		m = 0
		val = 0
		for i in range(len(x)):
			r = IT.Query(root, x[i])
			if m < len(r):
				m = len(r)
				val = x[i]
		return val	
def main():
	a = [[10,17], [15,25], [18,22], [21, 26], [16, 20]]
	iTree = IT.FromIntervals(a)
	inorder(iTree)
	print IT.Query(iTree, 24)
	IT.AllConflictingIntervals(iTree)
	print
	print "Number in max intervals = ", IT.FindNumInMaxIntervals(iTree)

def inorder(root):
	if root == None:
		return
	inorder(root.left)
	print "Node key = %s , Node intervals = %s"%(root.key, root.intervals)
	inorder(root.right)

if __name__ == "__main__":
	main()
