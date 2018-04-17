import sys
d = {
    0:"zero",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",

}


tens = {
    2:"twenty",
    3:"thirty",
    4:"forty",
    5:"fifty",
    6:"sixty",
    7:"seventy",
    8:"eighty",
    9:"ninety",
    100:"one hundred"
}


for line in sys.stdin:
    s = ""
    a = line.split()
    for n in a:
        if len(n) == 1:
            s = s + d[int(n)] + " "
        elif len(n) == 2 and n[0] == "1":
            s = s + d[int(n)] + " "
        elif len(n) == 2 and n[0] != "1" and n[1] != "0":
            s = s + tens[int(n[0])] + "-" + d[int(n[1])] + " "
        elif len(n) == 2 and n[0] != "1" and n[1] == "0":
            s = s + tens[int(n[0])] + " "
        elif n == "100":
            s = s + "one hundred" + " "
    print(s.strip())


