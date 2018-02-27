

def cap(s):
	if len(s) > 1:
		return s[0].upper() + s[1:len(s)-1] + s[-1].upper()
	else:
		return s 

def main():
	import sys
	for line in sys.stdin:
		cs = cap(line.strip())
		if len(cs) >= 2:
			print(cs)

if __name__ == '__main__':
	main()	