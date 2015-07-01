import random, array, sys
a = array.array('i')
for i in range(1000000):
	a.append(random.randint(1, 1000001))
	if len(a) > 1000:
		a.tofile(sys.stdout)
		del a[:]
if a:
	a.tofile(sys.stdout)
	del a[:]
