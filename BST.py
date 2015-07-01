import random
from time import sleep

class InIterator:
	def __init__(self, root):
		self.stack = []
		while root != None:
			self.stack.append(root)
			root = root.left
	def GetNext(self):
		if len(self.stack) != 0:
			result = self.stack.pop()
		else:
			return None
		rightTree = result.right
		while rightTree != None:
			self.stack.append(rightTree)
			rightTree = rightTree.left
		return result


class PostIterator:
	def __init__(self, root):
		self.stack = []
		self.PreProcess(root)
		
	def PreProcess(self, root):
		while root != None:
			if root.right != None:
				self.stack.append(root.right)
			self.stack.append(root)
			root = root.left
			
	def GetNext(self):
		while True:
			if len(self.stack) != 0:
				result = self.stack.pop()
				if len(self.stack) == 0:
					return result
			else:
				return None
			right = self.stack.pop()
			if result.right != None and result.right == right:
				self.stack.append(result)
				self.PreProcess(right)
			else:
				self.stack.append(right)
				return result
		


class Node:

	def __init__(self, left = None, right = None, value = -1):
		self.left = left
		self.right = right
		self.value = value
		self.leftNess = 0

class Tree:
	def __init__(self, root = None):
		self.root = root
	
	def inorder(self):
		self.inorderInt(self.root)

	def inorderInt(self, node):
		if node == None:
			return
		self.inorderInt(node.left)
		print "%s,(%s)" %(node.value,node.leftNess),
		self.inorderInt(node.right)

	def postorder(self):
		self.postorderInt(self.root)

	def postorderInt(self, node):
		if node == None:
			return
		self.postorderInt(node.left)
		self.postorderInt(node.right)
		print "%s," %node.value,

	def BFS(self, root):
		frontier = [root]
		while len(frontier):
			newNodes = []
			for node in frontier:
				print node.value,
				if node.left != None:
					newNodes.append(node.left)
				if node.right != None:
					newNodes.append(node.right)
			print
			frontier = newNodes


	def LCA(self, lv, rv):
		print "LCA = ",self.LCAInt(self.root, lv, rv).value
		path1 = []
		path2 = []
		if not self.FindPath(self.root, path1, lv) or not self.FindPath(self.root,
				path2, rv):
			print "LCA doesn't exist",
		i = 0
		while i < len(path1) and i < len(path2):
			if path1[i] != path2[i]:
				break
			i = i + 1
		print "LCA = ", path1[i-1].value

	def LCAInt(self, root, lv, rv):
		if root == None:
			return root
		if root.value == lv:
			return root
		if root.value == rv:
			return root
		llca = self.LCAInt(root.left, lv, rv)
		rlca = self.LCAInt(root.right, lv, rv)
		if llca != None and rlca != None:
			return root
		if llca == None:
			return rlca
		else:
			return llca
		
	def FindPath(self, root, a, k):
		if root == None:
			return False
		if root.value == k:
			a.append(root)
			return True
		a.append(root)
		if self.FindPath(root.left, a, k):
			return True
		if self.FindPath(root.right, a, k):
			return True
		a.pop()
		return False

	def PrintPaths(self, root, path):
		if root == None:
			for i in path:
				if i != None:
					print i.value,
			print
			return
		path.append(root)
		self.PrintPaths(root.left, path)
		#i = len(path) - 1
		#while i >= 0 and path[i] != root:
		#	path.remove(path[i])
		#	i = i - 1
		self.PrintPaths(root.right, path)
		path.pop()



	def iterInorder(self):
		self.iterInorderInt(self.root)
	
	def iterInorderInt(self, root):
		stack = []
		while root != None:
			stack.append(root)
			root = root.left

		while len(stack) != 0:
			root = stack.pop()
			if isinstance(root, Node):
				print "%s," %root.value,
				root = root.right
			while root != None:
				stack.append(root)
				root = root.left
	
	def FillTree(self):
		self.FillTreeInt(self.root, 0, 0)
	
	def FillTreeInt(self, node, level, leftNess):
		if level == 2:
			node.value = random.randint(1,100)
			node.leftNess = leftNess
			return
		node.value = random.randint(1, 100)
		node.leftNess = leftNess
		node.left = Node()
		node.right = Node()
		self.FillTreeInt(node.left, level+1, leftNess - 1)
		self.FillTreeInt(node.right, level+1, leftNess + 1)

	def CToDoublyLinkedList(self):
		ll = self.CToDoublyLinkedListInt(self.root)
		ll[0].left = ll[1]
		ll[1].right = ll[0]
		return ll
		
	
	def CToDoublyLinkedListInt(self, root):
		if root == None:
			return [None, None]
		ll = self.CToDoublyLinkedListInt(root.left)
		rl = self.CToDoublyLinkedListInt(root.right)
		head =tail =root
		if ll[1] != None:
			root.left = ll[1]
			ll[1].right = root
			head = ll[0]
		if rl[0] != None:
			root.right = rl[0]
			rl[0].left = root
			tail = rl[1]
		return [head, tail]
		
	def InBegin(self):
		it = InIterator(self.root)
		return it
	def PostBegin(self):
		it = PostIterator(self.root)
		return it

	def Print(self):
		self.PrintInt([self.root])
	
	def PrintInt(self, frontier, tabs = 5):
		nextFrontier = []
		tabsprinted = 0
		for node in frontier:
			if node != None:
				for i in range(tabs+node.leftNess-tabsprinted):
					print '\t',
					tabsprinted += 1
				print node.value,
				nextFrontier.append(node.left)
				nextFrontier.append(node.right)
		print
		if len(nextFrontier) != 0:
			self.PrintInt(nextFrontier)

# LongestPath(root) = max( LongestPath(root, left, path1) , LongestPath(root,
# right, path2),
	def LongestPath(self):
		heightMap = {}
		maxPathMap = {}
		self.FindHeight(self.root, heightMap)
		return self.LongestPathInt(self.root, heightMap, maxPathMap)

	def FindHeight(self, root, heightMap):
		if root == None:
			return 0;
		if root in heightMap:
			return heightMap[root]
		heightMap[root] = max(self.FindHeight(root.left, heightMap),
				self.FindHeight(root.right, heightMap)) + 1
		return heightMap[root]

	def LongestPathInt(self, root, heightMap, maxPathMap):
		if root == None:
			return 0
		if root in maxPathMap:
			return maxPathMap[root]
		m = 0
		m1 = 0
		m2 = 0
		if root.left != None:
			m = self.LongestPathInt(root.left, heightMap, maxPathMap)
			m1 = heightMap[root.left] + 1
		if root.right != None:
			m = max(m, self.LongestPathInt(root.right, heightMap, maxPathMap))
			m2 = heightMap[root.right] + 1
		maxPathMap[root] = max(m, m1+m2)
		return maxPathMap[root]





def TreeTravelsaltest():
	root = Node()
	temp = root
	tree = Tree(root)
	tree.FillTree()
	tree.Print()
	print "====Paths==="
	temp = root
	tree.PrintPaths(root, [])
	print "==BFS==="
	tree.BFS(root)
	print "=====================Inorder========================="
	tree.inorder()
	print ""
	tree.iterInorder()
	print ""
	it = tree.InBegin()
	result = it.GetNext()
	while result != None:
		print "%s," %result.value,
		result = it.GetNext()
	print
	print "=====================PostOrder========================"
	tree.postorder()
	print 
	it = tree.PostBegin()
	result = it.GetNext()
	while result != None:
		print "%s," %result.value,
		result = it.GetNext()
	root = temp
	print
	print root.left.left.value, root.left.right.value
	tree.LCA(root.left.left.value, root.left.right.value)
	root = temp
	print tree.LongestPath()
	root = temp
	ll = tree.CToDoublyLinkedList()
	temp = ll[0]
	while temp != ll[1]:
		print temp.value,
		temp = temp.right
	print temp.value
	temp = ll[1]
	while temp != ll[0]:
		print temp.value,
		temp = temp.left
	print temp.value


if __name__ == "__main__":
	TreeTravelsaltest()
