import sys
def strength(s):
    contains_number = False
    contains_lower = False
    contains_upper = False
    contains_special = False
    output = 0

    for char in s:
        if char.isdigit():
            contains_number = True
        elif char.isupper():
            contains_upper = True
        elif char.islower():
            contains_lower = True
        elif not char.isalpha() and not char.isdigit():
            contains_special = True

    if contains_number == True:
        output += 1
        # print("contains number")
    if contains_upper == True:
        output += 1
        # print("contains upper")
    if contains_lower == True:
        output += 1
        # print("contains lower")
    if contains_special == True:
        output += 1
        # print ("contains special")

    return output


def main():
    for line in sys.stdin:
        print(strength(line.strip()))

if __name__ == '__main__':
    main()



