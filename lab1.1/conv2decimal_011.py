def main():
	import sys
	for line in sys.stdin:
		x = line.split()[0][::-1]
		base = int(line.split()[1])
		i = 0
		output = 0
		while i < len(x):
			output += (int(x[i]) * (base ** i))
			i += 1
		print(output)

if __name__ == '__main__':
	main()