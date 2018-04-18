import sys
def palindrome(s):
	forward = s.lower()

	specials = []

	for char in forward:
		if not char.isalpha() and not char.isdigit():
			specials.append(char)

	# print(specials)


	for key in specials:
		if key in forward:
			forward = forward.replace(key, "")


	# print(forward)

	if forward == forward[::-1]:
		return True

	else:
		return False





def main():
	for line in sys.stdin:
		print(palindrome(line))


if __name__ == '__main__':
	main()