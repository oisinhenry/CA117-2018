import sys

s = sys.stdin.read().lower()

d = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0,
}

for char in s:
    if char == "a":
        d["a"] += 1
    elif char == "e":
        d["e"] += 1
    elif char == "i":
        d["i"] += 1
    elif char == "o":
        d["o"] += 1
    elif char == "u":
        d["u"] += 1

width = 0
for key in d:
    if len(str(d[key])) > width:
        width = len(str(d[key]))



s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
for k, v in s:
    print("{} : {:{:d}d}".format(k, v, width))