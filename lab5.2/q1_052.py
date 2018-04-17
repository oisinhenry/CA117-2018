def rotate(s):
    return s[-1] + s[:-1]

import sys
def main():
    s1 = sys.argv[1]
    rots = int(sys.argv[2])

    i = 0
    while i < rots:
        s1 = rotate(s1)
        i += 1
    print(s1)

if __name__ == '__main__':
    main()
