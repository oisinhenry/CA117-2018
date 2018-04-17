import sys
import random

iterations = 1000000
lotto_numbers = range(1, 48)

def main():
    s = set()
    for i in sys.argv[1:]:
        s.add(int(i))

    matches = {3:0, 4:0, 5:0, 6:0}

    for n in range(iterations):
        random_sample = set(random.sample(lotto_numbers, 6))
        match = len(s & random_sample)
        if match < 3:
            continue
        matches[match] += 1

    for (k, v) in sorted matches.items():
        


















if __name__ == '__main__':
    main()