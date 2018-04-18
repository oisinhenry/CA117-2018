def power(m, n):
    if n == 0:
        return 1

    n -= 1
    return m * power(m, n)