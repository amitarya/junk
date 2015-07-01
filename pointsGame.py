import copy

def ReturnWays(total, l, ll):
	if total < 0:
		return False
	if total == 0:
		return True
	if total >= 2:
		l.append(2)
		if ReturnWays(total - 2, l, ll):
			ll.append(copy.copy(l))
		l.pop()
	if total >= 3:
		l.append(3)
		if ReturnWays(total -3, l , ll):
			ll.append(copy.copy(l))
		l.pop()
	if total >= 7:
		l.append(7)
		if ReturnWays(total - 7, l, ll):
			ll.append(copy.copy(l))
		l.pop()

def main():
	l = []
	ll =[[]]
	ll.pop()
	ReturnWays(13, l, ll)
	print ll

if __name__ == "__main__":
	main()


