import random
class Node:
	def __init__(self, value):
		self.value = value
		self.nextNode = None

class List:
	def __init__(self):
		self.root = None

	def AddNode(self, value):
		temp = self.root
		if temp == None:
			self.root = Node(value)
			return True
		while temp.nextNode != None:
			temp = temp.nextNode
		temp.nextNode = Node(value)
	
	def PrintList(self):
		temp = self.root
		while temp != None:
			print temp.value,
			temp = temp.nextNode

	def RecReverse(self, node):
		if node.nextNode == None:
			self.root = node
			return node
		temp = self.RecReverse(node.nextNode)
		temp.nextNode = node
		node.nextNode = None
		return node

	def Reverse(self, k):
		temp = self.root
		counter = 0
		prev = None
		while temp != None:
			if (counter/k) %2 == 0:
				prev = self.ReverseInt(temp, k, prev)
				temp = prev.nextNode
				counter = counter + k
			else:
				prev = temp
				temp = temp.nextNode
				counter = counter + 1

	def ReverseInt(self, node, k, prevNode=None):
		temp = node
		stack = []
		while k>0 and temp.nextNode != None:
			stack.append(temp)
			temp = temp.nextNode
			k = k-1
		n = temp.nextNode
		c = prevNode
		if c == None:
			c = stack.pop()
			self.root = c
		while len(stack) > 0:
			c.nextNode = stack.pop()
			prevNode = c
			c = c.nextNode

		prevNode.nextNode = n
		return prevNode
	
def main():
	l = List()
	for i in range(3):
		l.AddNode(random.randint(1,100))
	l.PrintList()
	#l.Reverse(10)
	l.RecReverse(l.root)
	print
	l.PrintList()
	l.Reverse(3)
	print
	l.PrintList()

if __name__ == "__main__":
	main()


