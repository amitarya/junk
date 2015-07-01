class Node:
	def __init__(self, compchar=None, value=None):
		self.value = value
		self.compchar = compchar
		self.left = None
		self.middle = None
		self.right = None

class tTree:
	def __init__(self):
		self.root = None
	
	def put(self, key, value):
		if len(key) == 0:
			return
		if self.root == None:
			self.root = Node(key[0])
		self.putI(self.root, key, value, 1)
	
	def putI(self, node, key, value, level):
		if level == len(key) - 1:
			node.value = value
			return
		if node.compchar == key[level]:
			if node.middle == None:
				node.middle = Node(key[level])
			self.putI(node.middle, key, value, level + 1)
		elif node.compchar > key[level]:
			if node.left == None:
				node.left = Node(key[level])
			self.putI(node.left, key, value, level + 1)
		else:
			if node.right == None:
				node.right = Node(key[level])
			self.putI(node.right, key, value, level)

	def get(self, key):
		node = self.getI(self.root, key, 0)
		if node != None and node.value != None:
			return node.value
		else:
			return -1
	
	def getI(self, node, key, level):
		if level == len(key) - 1 or node == None:
			return node
		if node.compchar == key[level]:
			return self.getI(node.middle, key, level + 1)
		elif key[level] < node.compchar:
			return self.getI(node.left, key, level)
		else:
			return self.getI(node.right, key, level)

def main():
	T = tTree()
	T.put("amit", 5)
	T.put("ravi", 6)
	T.put("arya", 7)
	T.put("ami", 4)
	print T.root.middle.compchar
	print T.root.middle.middle.compchar
	print T.get("amit")
	print T.get("ami")
	T.put("amit", 9)
	print T.get("amit")
	#T.delete("ami")
	print T.get("amit")
	print T.get("ami")


if __name__ == "__main__":
	main()

