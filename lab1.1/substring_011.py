def substring(s,x):
	if s in x:
		return True
	else:
		return False

def main():
	import sys
	for line in sys.stdin:
		s1 = line.split()[0].lower()
		s2 = line.split()[1].lower()
		print(substring(s1, s2))

if __name__ == '__main__':
	main()