import sys
class ST:
	def __init__(self, lvalue, rvalue, a):
		if lvalue > rvalue:
			return
		if lvalue == rvalue:
			self.maximum = a[lvalue]
		self.left = None
		self.right = None
		self.lvalue = lvalue
		self.rvalue = rvalue
		if lvalue < rvalue:
			mid = (lvalue + rvalue)/2
			self.left = ST(lvalue, mid, a)
			self.right = ST(mid+1, rvalue, a)
			self.maximum = max(self.left.maximum, self.right.maximum)


	@staticmethod
	def TreeMax(root, lvalue, rvalue):
		if lvalue > rvalue:
			return 0
		if root.lvalue == root.rvalue:
			return root.maximum
		if root.lvalue == lvalue and root.rvalue == rvalue:
			return root.maximum
		mid = (root.lvalue + root.rvalue)/2
		return max(ST.TreeMax(root.left, lvalue, mid), ST.TreeMax(root.right, mid+1,
		rvalue))


def main():
	a = [4,2,5,7,6,8]
	root = ST(0, len(a)-1, a)
	node = root
	while root != None:
		print root.lvalue, root.rvalue, root.maximum
		root = root.left
	root = node
	while root != None:
		print root.lvalue, root.rvalue, root.maximum
		root = root.right
	print ST.TreeMax(node, 3,4)
if __name__ == "__main__":
	main()
