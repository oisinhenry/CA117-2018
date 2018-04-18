import sys

def tokens(s):
	return len(s.split())
	


def main():
	total = 0
	for line in sys.stdin:
		total = total + tokens(line)
	print(total)


if __name__ == '__main__':
	main()