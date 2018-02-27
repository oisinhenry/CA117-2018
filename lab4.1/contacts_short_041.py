import sys

lines = open(sys.argv[1])
contacts = {}

for line in lines:
    line = line.strip().split()
    contacts[line[0]] = line[1]


for line in sys.stdin:
    print("Name: {}".format(line.strip()))
    if line.strip() in contacts:
        print("Phone: {}".format(contacts[line.strip()]))
    else:
        print("No such contact")





