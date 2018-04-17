import sys

s = sys.argv[1]

new_s = ""
if len(s) > 1:
    i = 1
    while i < len(s):
        new_s += s[i]
        new_s += s[i-1]
        i += 2
    if len(s) % 2 != 0:
        new_s += s[-1]



else:
    new_s = s

print(new_s)