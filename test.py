#! /usr/bin/env python
import math

def f(number_of_iterations):
	L = [1]
	for n in range(2, number_of_iterations):
		print(n)
		L = [sum(L[:i]) for i in range(n-1, -1, -1)]
		print(L)
	return numerical_approx(2*L[0]*len(L)/sum(L),digits=50)

def main(argv):
	print('amit')
	print(f(argv))

if __name__ == "__main__":
	main(10)

