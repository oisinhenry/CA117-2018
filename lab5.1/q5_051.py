import sys

def seconds(t):
    tokens = t.split(":")
    n1 = int(tokens[0]) * 60
    n2 = int(tokens[1])
    return n1 + n2


def main():
    d = {}


    for line in sys.stdin:
        tokens = line.split()
        name = tokens[0]
        try:
            time = min(tokens[1:], key=seconds)
        except:
            continue
        d[time] = name

    best = min(d.keys(), key=seconds)

    print("{} : {}".format(d[best], best))


if __name__ == '__main__':
    main()




