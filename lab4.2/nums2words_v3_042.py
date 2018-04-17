import sys

trans = {}
for line in open(sys.argv[1]):
    tokens = line.split()
    trans[tokens[0]] = tokens[1]






d = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}

for line in sys.stdin:
    a = []
    for key in line.split():
        a.append(int(key))
    
    print(" ".join([trans[d[k]] for k in a]))