import sys
lines = []
def main():
	for line in sys.stdin:
		lines.append(line.strip().lower())

	print([line for line in lines if reverse_in_list(line)])




def bsearch(a, s):
	low = 0
	high = len(a)

	while low < high:
		mid = (low + high) // 2

		if a[mid] < s:
			low = mid + 1
		else:
			high = mid

		return a[low]




def reverse_in_list(s):
	if bsearch(lines, s[::-1]).strip() == s[::-1].strip():
		return True




if __name__ == '__main__':
	main()


















   # low = 0
   # high = len(a)

   # while low < high:
   #    mid = (low + high) / 2

   #    if a[mid] < q:
   #       low = mid + 1
   #    else:
   #       high = mid

   # return low