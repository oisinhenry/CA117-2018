import sys
import string



def strip_punc(s_word):
    return s_word.rstrip('?:!.,;')





d = {}
s = sys.stdin.read()

s = s.lower()

words = s.split()
a = []

for word in words:
    a.append(strip_punc(word))


for word in a:
    if len(word) > 3:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1




new_d = {}

for key in d:
    if d[key] >= 3:
        new_d[key] = d[key]
width = 0
for key in new_d:
    if len(key) > width:
        width = len(key)





for (k, v) in sorted(new_d.items()):
    print('{:>{:d}s} : {:{:d}d}'.format(k, width, v, 2))


















