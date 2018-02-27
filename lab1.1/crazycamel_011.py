def ccamel(a):
	b = []
	for s in a:
		s = s[::-1]
		s = s.capitalize()
		s = s[::-1]
		b.append(s)
	return " ".join(b).strip()

def main():
	import sys
	for line in sys.stdin:
		li = line.split()
		print(ccamel(li))




if __name__ == '__main__':
	main()