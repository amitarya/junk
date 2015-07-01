def GetMapFromvector(v):
	m = {}
	for i in range(len(v)):
		if v[i] != 0:
			m[i] = v[i]
	return m

def DotProduct(m1, m2):
	s = 0
	for key in m1:
		if key in m2:
			s = s + m1[key]*m2[key]
	return s
def main():
	v1 = [6,2,0,0,0,0,6]
	v2 = [1,0,4,0,0,-1, 2]
	m1 = GetMapFromvector(v1)
	m2 = GetMapFromvector(v2)
	print DotProduct(m1, m2)


if __name__ == "__main__":
	main()
