import sys
words = []
for line in sys.stdin:
    new_line = line.lower().strip()
    if new_line.count("e") == 1 and new_line.count("v") == 1 and new_line.count("i") == 1 and new_line.count("l") == 1:
        if new_line.find("e") < new_line.find("v") and new_line.find("v") < new_line.find("i") and new_line.find("i") < new_line.find("l"):

            words.append(line)

for line in words:
    print(line.strip())