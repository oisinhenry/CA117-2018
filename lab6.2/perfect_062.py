import sys

def sumFac(x):
    return sum([n for n in range(1, x) if x % n == 0])



def isPerfect(n):
    if sumFac(n) == n:
        return True
    else:
        return False

def main():
    for line in sys.stdin:
        print(isPerfect(int(line.strip())))


if __name__ == '__main__':
    main()

# print(sumFac(28))
# print(isPerfect(28))