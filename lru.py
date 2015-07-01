class lruCache:
	def __init__(self, size):
		self._map = {}
		self._listHead = None
		self._listTail = None
		self.size = size
		self.items = 0
	def Read(self, key):
		value = None
		if key in self._map:
			lp = self._map[key]
			if lp.left == None:
				value = lp.value
				return value
			if lp.right == None:
				self._listTail = self._listTail.left
			if lp.left != None:
				lp.left.right = lp.right
			if lp.right != None:
				lp.right.left = lp.left
			temp = self._listHead
			self._listHead.left = lp
			self._listHead = lp
			self._listHead.right = temp
			value = lp.value
		return value

	def Print(self):
		print "=====Map===="
		for key in self._map:
			print key, self._map[key].value
		print "=====List===="
		temp = self._listHead
		while temp != None:
			print temp.value
			temp = temp.right

	def Put(self, key, value):
		self._map[key] = Node(key, value)
		if self._listHead == None:
			self._listHead = self._listTail = self._map[key]
		else:
			temp = self._listHead
			temp.left = self._map[key]
			self._listHead = self._map[key]
			self._listHead.right = temp
		if self.items == self.size:
			self._map.pop(self._listTail.key, None)
			self._listTail = self._listTail.left
			self._listTail.right = None
		else:
			self.items = self.items + 1




class Node:
	def __init__(self, key=None, value=None, left=None, right = None):
		self.value = value
		self.left = left
		self.right = right
		self.key = key

def TestlruCache():
	lC = lruCache(3)
	lC.Put(2, "amit")
	lC.Put(3, "arya")
	lC.Put(5, "ram")
	print lC.Print()
	lC.Read(2)
	lC.Put(6, "mohan")
	print lC.Print()
	

def TestLRUPutAndRead():
	print "----start TestLRUPut ----"
	lc = lruCache(3)
	lc.Put(1, "amit")
	lc.Put(2, "arya")
	lc.Put(3, "ram")
	lc.Put(4, "mohan")
	lc.Read(4)
	lc.Read(3)
	lc.Read(2)
	lc.Print()

def main():
	TestlruCache()
	#TestLRUPutAndRead()

if __name__ == "__main__":
	main()

