def caps(a):
	b = []
	for s in a:
		s = s.capitalize()
		b.append(s)
	return " ".join(b).strip()

def main():
	import sys
	for line in sys.stdin:
		li = line.split()
		print(caps(li))




if __name__ == '__main__':
	main()