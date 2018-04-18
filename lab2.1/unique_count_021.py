import sys
import string

s = sys.stdin.read()

for char in string.punctuation:
	if char in s:
		s = s.replace(char, "")

s = s.lower()

a = s.split()
words = []
total = 0
for word in a:
	if word not in words:
		total += 1
		words.append(word)

print(total)