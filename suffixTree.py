class Node:
	def __init__(self):
		self._map = {'$':None}

class SuffixTree:
	def __init__(self):
		self.root = Node()
	def AddWord(self, string):
		self.AddWordInt(string, self.root)
	def AddWordInt(self, string, root,index = 0):
		if index == len(string):
			return
		if string[index] not in root._map:
			root._map[string[index]] = Node()
		self.AddWordInt(string, root._map[string[index]], index+1)
	
	def IsMember(self, string):
		return self.IsMemberInt(string, self.root)
	
	def IsMemberInt(self, string, root, index=0):
		if index == len(string):
			return True
		if string[index] in root._map:
			return self.IsMemberInt(string, root._map[string[index]], index+1)
		else:
			return False
	
def main():
	st = SuffixTree()
	st.AddWord("foo")
	st.AddWord("bar")
	st.AddWord("baz")
	print st.IsMember("baz")

if __name__ == "__main__":
	main()

