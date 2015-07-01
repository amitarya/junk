_map = {1:'a', 2:'b',3:'c',4:'d',5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j',
		11:'k', 12:'l',13:'m',14:'n', 15:'o',}

def InputInterpret(s, i=0, output=[]):
	if i == len(s):
		yield output
		return
	num = ord(s[i]) - 48
	output.append(_map[num])
	for x in InputInterpret(s, i+1, output):
		yield x
	output.pop()
	if i < len(s) -1:
		num = num*10 + ord(s[i+1]) - 48
		if num in _map:
			output.append(_map[num])
			for x in InputInterpret(s, i+2, output):
				yield x
			output.pop()
	
def main():
	for value in InputInterpret("123415"):
		print ''.join(value)
	
if __name__ == "__main__":
	main()

