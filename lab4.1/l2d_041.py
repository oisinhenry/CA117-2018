import sys

def l2d(file):
    a = file.read().split()

    keys = a[:len(a)//2]
    ints = a[len(a)//2:]
    d = {}
    i = 0
    while i < len(keys):
        d[keys[i]] = ints[i]
        i += 1


    return d

