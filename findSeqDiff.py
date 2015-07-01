def DiffSeq(seq1, seq2):
	return DiffSeqInt(seq1, seq2, 0)

def DiffSeqInt(seq1, seq2, tol):
	while True:
		val1 = next(seq1, None)
		val2 = next(seq2, None)
		print val1, val2
		if val1 == None or val2 == None:
			break
		if val1 != val2:
			if tol > 0:
				val1next = next(seq1, None)
				val2next = next(seq2, None)
				if (val1 == val2next and val1next == None) or (val2 == val1next or val1next == val2next:
					return DiffSeqInt(seq1, seq2, tol-1)
			else:
				return False
	if val1 != None:
		tol = tol - 1
		while tol > 0:
			val1 = next(seq1, None)
			if val1 == None:
				return True
			tol = tol - 1
		return False
	elif val2 != None:
		tol = tol - 1
		while tol > 0:
			val2 = next(seq2, None)
			if val2 == None:
				return True
			tol = tol - 1
		return False
	else:
		return True

def main():
	seq1 = (1,2,3,0,4)
	seq2 = (1,2,3,4,5)
	print DiffSeqInt(iter(seq1), iter(seq2), 1)

if __name__ == "__main__":
	main()
