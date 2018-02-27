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
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1


for (k, v) in sorted(d.items()):
    print('{} : {}'.format(k, v))


















