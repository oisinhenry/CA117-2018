import sys

d = {0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine", 10:"ten"}

for line in sys.stdin:
    a = []
    for key in line.split():
        try:
            a.append(int(key))
        except ValueError:
            a.append(key)

    
    s = ""
    for key in a:
        try:
            s = s + d[key] + " "
        except:
            s = s + "unknown "

    print(s.strip())