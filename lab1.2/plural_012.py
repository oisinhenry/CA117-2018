import sys
def plural(s):
    if s.endswith("ch") or s.endswith("sh") or s.endswith("x") or s.endswith("s") or s.endswith("z"):
        return s + "es"
    elif s.endswith("y") and s[len(s)-2] != "a" and s[len(s)-2] != "e" and s[len(s)-2] != "i" and s[len(s)-2] != "o" and s[len(s)-2] != "u":
        return s[:len(s)-1] + "ies"
    elif s.endswith("f"):
        return s[:len(s)-1] + "ves"
    elif s.endswith("fe"):
        return s[:len(s)-2] + "ves"
    elif s.endswith("o"):
        return s + "es"
    else:
        return s + "s"

def main():
    for line in sys.stdin:
        print (plural(line.strip()))


if __name__ == '__main__':
    main()
