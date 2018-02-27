import sys

lines = open(sys.argv[1])
contacts = {}

for line in lines:
    line = line.strip().split()
    contacts[line[0]] = line[1]


for line in sys.stdin:
    print("Name: {}".format(line))
    if line in contacts:
        print("Phone: {}".format(contacts[line]))
    else:
        print("No such contact")





