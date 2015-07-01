def Balance(string):
	print string
	stack = []
	words = []
	for i in range(len(string)):
		if string[i] == '(':
			stack.append(len(words))
			words.append(string[i])
		elif string[i] == ')':
			if len(stack) != 0:
				stack.pop()
				words.append(string[i])
		else:
			words.append(string[i])
	while len(stack) != 0:
		words.pop(stack.pop())
	return ''.join(words)

def main():
	print Balance("a((mit)())")

if __name__ == "__main__":
	main()




