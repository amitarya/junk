class Node:
	def __init__(self, value=None):
		self.value = value
		self.children = {}

class Trie:
	def __init__(self):
		self.root = Node()
	
	def put(self, key, value):
		self.putI(self.root, key, value, 0)
		
	def putI(self, node, key, value, i):
		if i == len(key):
			node.value = value
			return
		if key[i] not in node.children:
			node.children[key[i]] = Node()
		self.putI(node.children[key[i]], key, value, i+1)

	def get(self, key):
		node = self.getI(self.root, key, 0)
		if node != None and node.value != None:
			return node.value
		else:
			return -1
	def getI(self, node, key, level):
		if level == len(key):
			return node
		if key[level] in node.children:
			return self.getI(node.children[key[level]], key, level+1)
		else:
			return None
	
	def delete(self, key):
		self.deleteI(self.root, key, 0)
	
	def deleteI(self, node, key, level):
		if level == len(key):
			if node.value != None:
				node.value = None
				return True
			else:
				return False
		if key[level] in node.children:
			if self.deleteI(node.children[key[level]], key, level+1) and node.children[key[level]].value == None:
				if len(node.children[key[level]].children) == 0:
						node.children[key[level]] = None
				return True
			else:
				return False




def main():
	T = Trie()
	T.put("amit", 5)
	T.put("ravi", 6)
	T.put("arya", 7)
	T.put("ami", 4)

	print T.get("amit")
	print T.get("ami")
	T.put("amit", 9)
	print T.get("amit")
	T.delete("ami")
	print T.get("amit")
	print T.get("ami")


if __name__ == "__main__":
	main()
