import sys

lines = []

for line in sys.stdin:
    lines.append(line)

holes = {}
# number : {par : index}

pars = lines[0].split()
indices = lines[1].split()
lines = lines[2:]

for i in range(0, 17):
    holes[i] = {int(pars[i]) : int(indices[i])}

print(holes)



players = {}

score_d = {
    -7: 9,
    -6: 8,
    -5: 7,
    -4: 6,
    -3: 5,
    -2: 4,
    -1: 3,
    0: 2,
    1: 1,
    2: 0,

}

current = lines[0].split()[1:]
handicap = lines[0].split()[0]
# i = 0
# while i < len(current):
    # if 


