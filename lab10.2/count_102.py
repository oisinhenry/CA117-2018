def count_letters(string):

	if len(string) == 0:
		return 0


	return 1 + count_letters(string[:-1])
