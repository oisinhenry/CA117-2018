import sys
def anagram(s0, s1):
    chars = False
    for char in s0:
        if char in s1:
            chars = True
        else:
            chars = False
    if chars == True and len(s0) == len(s1):
        return True
    else:
        return False


def main():
    for line in sys.stdin:
        left = line.split()[0]
        right = line.split()[1]
        print(anagram(left, right))


if __name__ == '__main__':
    main()

