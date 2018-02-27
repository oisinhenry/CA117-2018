import sys
filename = sys.argv[1]
lines = []
highest = 0
best = None

def openfile(filename):
    try:
        f_in = open(filename, "r")
        return f_in

    except FileNotFoundError:
        print("Could not open file: {}".format(filename))
    except PermissionError:
        print("Permission error on file: {}")
    



def main():
    highest = 0
    best = []
    for line in openfile(filename):
        try:
            if int(line.split()[0]) > highest:
                highest = int(line.split()[0])
                if len(best) == 0:
                    best.append(" ".join(line.split()[1:]).strip())
                else:
                

                    best[0] = " ".join(line.split()[1:]).strip()
            elif int(line.split()[0]) == highest:
                best.append(" ".join(line.split()[1:]).strip())

        except ValueError:
            print("Invalid mark {} encountered. Skipping.".format(line.split()[0]))



    if len(best) > 1:
        best_students = ", ".join(best).strip()
    else:
        best_students = best[0].strip()



    print("Best student(s): {}".format(best_students))

    print("Best mark: {}".format(highest))

if __name__ == '__main__':
    main()


        

