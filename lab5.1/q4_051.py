import sys
a = []
for line in sys.stdin:
    a.append(int(line.strip()))

mean = sum(a) / len(a)
mode = max(set(a), key=a.count)

if len(a) % 2 == 1:
    sort_a = sorted(a)
    median = sort_a[len(sort_a) // 2]

else:
    sort_a = sorted(a)
    n1 = sort_a[len(sort_a) // 2]
    n2 = sort_a[len(sort_a) // 2 - 1]
    median = (n1 + n2) / 2

print("Mean: {:.1f}".format(mean))
print("Mode: {}".format(float(mode)))
print("Median: {}".format(float(median)))
