import sys
filename = sys.argv[1]
lines = []
highest = 0
best = None

try:
    f_in = open(filename, "r")

except FileNotFoundError:
    print("Could not open file: {}".format(filename))
except PermissionError:
    print("Permission error on file: {}")
    




for line in f_in:
    if int(line.split()[0]) > highest:
        highest = int(line.split()[0])
        best = " ".join(line.split()[1:]).strip()

print("Best student: {}".format(best))

print("Best mark: {}".format(highest))


        

