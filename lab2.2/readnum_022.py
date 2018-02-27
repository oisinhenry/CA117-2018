import sys

while True:
    try:
        x = sys.stdin.readline().strip()
        d = int(x)
        print("Thank you for " + x)
        break
    except ValueError:
        print("{} is not a number".format(x))
