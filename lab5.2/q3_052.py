def build_dictionary(filename):
    d = {}
    for line in open(filename):
        tokens = line.split()
        d[tokens[0]] = int(tokens[1])

    return d


def extract_range(d, low, high):
    new_d = {}
    for k, v in d.items():
        if low <= v and v <= high:
            new_d[k] = v
    return new_d

