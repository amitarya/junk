import sys, array, struct
def readChunk(f):
	while True:
		a = array.array('B')
		a.fromstring(f.read(2000))
		if not a:
			break
		for value in a:
			yield value

def ProcessInput(m):
	f = open('emailContacts.txt', 'r')
	line = ""
	for c in readChunk(f):
		eol = False
		if chr(c) != '\n':
			line = line + chr(c)
		else:
			eol = True
		if eol and len(line) > 0:
			values = line.split(':')
			contact = values[0]
			emails = values[1].split(',')
			for email in emails:
				if email in m:
					m[email].append(contact)
				else:
					m[email] = [contact]
			line = ""

def main():
	m = {}
	ProcessInput(m)
	for k in m:
		print k,
		for value in m[k]:
			print value,
		print

if __name__ == "__main__":
	main()
	
		
			

