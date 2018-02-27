def main():
	import sys
	n = int(sys.argv[1])

	a = []
	i = 0
	stars = 1
	while i < n:
		print(((" " * int(n - stars)) + "* " * stars).rstrip())
		a.append((" " * int(n - stars)) + "* " * stars)
		i += 1
		stars += 1

	# print(("* ") * n)

	i = 0
	while i < len(a)-1:
		print((a[len(a)-2-i]).rstrip())
		i += 1

if __name__ == '__main__':
	main()