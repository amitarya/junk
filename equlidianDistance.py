import heapq, random
def FindMin10Eqilidian(a, heap):
	count = 0
	for (i,j,k) in a:
		dist = pow(pow(i,2)+pow(j,2) + pow(k,2), 0.5)
		heapq.heappush(heap, (-dist,(i,j,k)))
		count = count + 1
		if count > 5:
			heapq.heappop(heap)

def main():
	a = []
	for i in range(50):
		a.append((random.randint(0,10), random.randint(0,10),
			random.randint(0,10)))
	print a
	h = []
	FindMin10Eqilidian(a,h)
	for v in h:
		print v

if __name__ == "__main__":
	main()


