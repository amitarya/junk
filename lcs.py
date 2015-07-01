# lcs(i, j) = max(lcs(i+1,j),lcs(i, j+1), lcs(i+1,j+1)+ a[i]==a[j]?1:0)
import sys
def lcs(a, b, i, j, a_size, b_size, c):
	if i > a_size - 1 or j > b_size - 1:
		return 0
	if i == a_size-1 and j == b_size-1:
		if a[i]==b[j]:
			return 1
		else:
			return 0
	if c[i][j] < sys.maxint:
		print "c[%s,%s]=%s"%(i,j,c[i][j])
		return c[i][j]
	flag = 0
	if a[i]==b[j]:
		flag = 1
	c[i][j] = max(lcs(a, b, i+1,j, len(a), len(b), c),lcs(a,b,i, j+1,len(a),
	len(b),c), (lcs(a,b,i+1, j+1,len(a), len(b),c)+flag))
	return c[i][j]

def max(a,b,c):
	return max2(max2(a,b),c)

def max2(a,b):
	if a>b:
		return a
	else:
		return b
def main():
	a = [1,3,4,5,6,7]
	b = [1,2,3,4,5,8]
	c = [[sys.maxint for i in range(len(a))] for i in range(len(b))]
	print "%s" %lcs(a, b, 0,0, len(a), len(b), c)

if __name__ == "__main__":
	main()
	print max(5,1,2)

