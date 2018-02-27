import sys

words_d = {}

def main():
    words = [word.strip() for word in sys.stdin if 5 <= len(word.strip())]
    for word in words:
        words_d[word.casefold()] = True

    print([w for w in words if w[::-1].casefold() in words_d])

if __name__ == '__main__':
    main()