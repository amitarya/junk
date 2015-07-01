class Node:
	def __init__(self):
		self.value = None
		self.nextI = None


def FlattenList(l):
	temp = l
	prev = None
	while temp != None:
		if isinstance(temp.value, Node):
			FlattenList(temp.value)
			temp2 = temp.value
			while temp2.nextI != None:
				temp2 = temp2.nextI
			temp3 = temp.nextI
			prev.nextI = temp.value
			prev = temp2
			temp2.nextI = temp3
			temp = temp3
		else:
			prev = temp
			temp = temp.nextI



def main():
	root = Node()
	root.value = 5
	root.nextI = Node()
	root.nextI.value = Node()
	root.nextI.nextI = Node()
	root.nextI.nextI.value = 6
	root.nextI.nextI.nextI = None
	root.nextI.value.value = 7
	root.nextI.value.nextI = Node()
	root.nextI.value.nextI.value = Node()
	root.nextI.value.nextI.value.value = 9
	root.nextI.value.nextI.value.nextI = None
	root.nextI.value.nextI.nextI = None
	FlattenList(root)
	temp = root
	while temp != None:
		print temp.value
		temp = temp.nextI	

if __name__ == "__main__":
	main()
