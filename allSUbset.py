import copy

def main():
	a = ['1','2','3']
	v = powerSet(a)
	print v
	ps = [[]]
	powerSet1(a, ps)
	print ps
	perm(['1','2','3'])
	for v in powerSetBest(a, []):
		for i in v:
			print i,
		print

def powerSet(a, index = 0):
	if index >= len(a) - 1:
		return [[], [a[index]]]
	v = powerSet(a, index+1)
	s = powerSet(a, index+1)
 	for st in s:
		st.append(a[index])
		v.append(st)
	return v
def powerSetBest(a, s, index = 0):
	if index >= len(a):
		yield s
	else:
		s.append(a[index])
		for x in powerSetBest(a, s, index+1):
			yield x
		s.pop()
		for x in powerSetBest(a, s, index+1):
			yield x


def powerSet1(a, v, index = 0):
	if index > len(a) - 1:
		return
	s = copy.deepcopy(v)
	for st in s:
		st.append(a[index])
		v.append(st)
	powerSet1(a, v, index+1)

def perm(a, index = 0):
	if index > len(a) - 1:
		print ''.join(a)
	for pos in range(index, len(a)):
		swap(a, pos, index)
		perm(a, index+1)
		swap(a, pos, index)
	
def swap(a, pos, index):
	temp = a[pos]
	a[pos] = a[index]
	a[index] = temp

	
if __name__ == "__main__":
	main()


