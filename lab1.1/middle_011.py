def middle(s):
	if len(s) % 2 == 0:
		return "No middle character!"
	else:
		return s[int(len(s) / 2)]

def main():
	import sys
	for line in sys.stdin:
		mid = middle(line.strip())
		print(mid)

if __name__ == '__main__':
	main()