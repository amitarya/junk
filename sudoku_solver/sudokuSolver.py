#! /usr/bin/env python

import sys
import random
def Place(a, row, col, size, value):
	if row > size or col > size:
		return False
	for i in range(size):
		if i == row:
			continue
		if a[i][col] == value:
			return False
	
	for j in range(size):
		if j == col:
			continue
		if a[row][j] == value:
			return False
	# check in the 3x3 submatirx
	subrow = row - row%3
	subcol = col - col%3
	for i in range(subrow, subrow+3):
		for j in range(subcol, subcol+3):
			if row == i and col == j:
				continue
			if value == a[i][j]:
				return False
	return True

def sudokuSolver(a, size):
	(row, col) = FindUnsolved(a, size)
	if (row, col) == (-1, -1):
		if checkSolved(a, size) == True:
			print "Solved"
			return True
		else:
			return False
	for i in range(size):
		if Place(a, row, col, size, i+1) == True:
			a[row][col] = i+1
			if sudokuSolver(a, size) == True:
				return True
			else:
				a[row][col] = 0
	return False

def FindUnsolved(a, size):
	for i in range(size):
		for j in range(size):
			if a[i][j] == 0:
				return (i, j)
	return (-1, -1)
def checkSolved(a, size):
	for i in range(size):
		for j in range(size):
			if Place(a,i,j,size,a[i][j]) == False:
				return False
	return True

def main():
	a = [[0 for i in range(9)] for i in range(9)]
	for i in range(9):
		j = random.randint(0,8)
		value = random.randint(1,9)
		while Place(a, i, j, 9, value) == False:
			value = random.randint(1,9)
		a[i][j] = value
	print "======================BEFORE======================="
	prettyprint(a)
	print "========================AFTER======================"
	sudokuSolver(a, 9)
	prettyprint(a)

def prettyprint(a):
	for i in xrange(9):
		for j in xrange(9):
			if j == 0:
				sys.stdout.write("|")
			print("%s," % a[i][j]),
			if j == 8:
				print "|"
if __name__ == "__main__":
	main()

