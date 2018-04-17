import sys

def get_roots(a, b, c):
    ans = b**2 - (4*a*c)
    if ans < 0:
        return None


    root1 = (-b + ans**0.5)/(2*a)
    root2 = (-b - ans**0.5)/(2*a)

    return root1, root2

for line in sys.stdin:
    a, b, c = map(int, line.split())
    roots = get_roots(a, b, c)

    if roots == None:
        print(None)
    else:
        print("r1 = {}, r2 = {}".format(*roots))