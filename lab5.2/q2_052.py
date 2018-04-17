import sys
words = []
for line in sys.stdin:
    new_line = line.lower().strip()
    if new_line.count("a") == 1 and new_line.count("e") == 1 and new_line.count("i") == 1 and new_line.count("o") == 1 and new_line.count("u") == 1:
        if new_line.find("a") < new_line.find("e") and new_line.find("e") < new_line.find("i") and new_line.find("i") < new_line.find("o") and new_line.find("o") < new_line.find("u"):

            words.append(line)

for line in words:
    print(line.strip())