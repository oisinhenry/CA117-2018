def contains(chars, s):	#call for each character and check if all true
	for c in chars:
		if c in s:
			s = s.replace(c,"")
		elif c not in s:
			return False
	return True



def main():
	import sys
	for line in sys.stdin:
		c = line.split()[0].lower()
		s = line.split()[1].lower()
		print(contains(c,s))





		


if __name__ == '__main__':
	main()