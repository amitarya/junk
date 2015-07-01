#Recursive backtracking solution for all src and dest words.
#visualize its like DFS.
import copy
def PrintAllDictWords(src, dest, index, d):
	if index == len(src):
		if "".join(src) in d:
			print ''.join(src)
			#level["".join(src)] = index
		return
	PrintAllDictWords(src, dest, index+1, d)
	temp = src[index]
	src[index] = dest[index]
	PrintAllDictWords(src, dest, index+1, d)
	src[index] = temp

def PrintAllDictWordsBFS(src, dest, index, d):
	level = {''.join(src):0}
	frontier = [src]
	counter = 1
	l = 0
	while len(frontier) != 0:
		nf = []
		exists = True
		for word in frontier:
			for i in range(len(word)):
				if word[i] != dest[i]:
					exists = False
					break
			if exists:
				break
		l = l+1
		for word in frontier:
			for i in range(len(src)):
				temp = word[i]
				word[i] = dest[i]
				if ''.join(word) in d:
					if ''.join(word) not in level:
						nf.append(copy.deepcopy(word))
						print ''.join(word)
						level[''.join(word)] = l
				word[i] = temp
		print nf
		frontier = nf
	


		counter = counter + 1
		frontier = nf



				


def main():
	PrintAllDictWords(list("CAT"), list("DOG"), 0, set(["CAT", "COT", "DOT",
		"DOG", "COG"]))
	print "***BFS***"
	PrintAllDictWordsBFS(list("CAT"), list("DOG"), 0, set(["CAT", "COT", "DOT",
		"DOG", "COG"]))
		
		#PrintAllDictWordsBFS(list("DUMB"), list("HILK"), 0, set(["DUMB", "HUMB", "HULB", "HULK",
		#"HILK"]))

if __name__ == "__main__":
	main()
