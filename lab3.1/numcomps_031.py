import sys
num = int(sys.argv[1])

numbers = [n for n in range(1, num + 1)]



def func_x(a):
    b = []
    for key in a:
        if key % 3 == 0:
            b.append("X")
        else:
            b.append(key)
    return b


def is_prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                return False
        return True
    else:
        return False



def getprimes(li):
    output = []
    for n in li:
        if is_prime(n):
            output.append(n)
    return output




print("Multiples of 3: {}".format([n for n in numbers if n % 3 == 0]))
print("Multiples of 3 squared: {}".format([n ** 2 for n in numbers if n % 3 == 0]))
print("Multiples of 4 doubled: {}".format([n * 2 for n in numbers if n % 4 == 0]))
print("Multiples of 3 or 4: {}".format([n for n in numbers if n % 3 == 0 or n % 4 == 0]))
print("Multiples of 3 and 4: {}".format([n for n in numbers if n % 3 == 0 and n % 4 == 0]))
print("Multiples of 3 replaced: {}".format(func_x(numbers)))
print("Primes: {}".format(getprimes(numbers)))
# def func_x(a):
#     b = []
#     for key in a:
#         if key % 3 == 0:
#             b.append("X")
#         else:
#             b.append(key)
#     return b

# def primes(a):
#     b = []
#     for no in a:

