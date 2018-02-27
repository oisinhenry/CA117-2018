import sys
from math import pi

def main():
    x = int(sys.argv[1])
    print("{:.{}f}".format(pi, x))


if __name__ == '__main__':
    main()


















# "{:.{}f}".format(pi)(x)
# 3.xxxxx
