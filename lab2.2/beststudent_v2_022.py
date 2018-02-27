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
    best = None
    try:
        for line in openfile(filename):
        
            if int(line.split()[0]) > highest:
                highest = int(line.split()[0])
                best = " ".join(line.split()[1:]).strip()
        # except ValueError:
        #     print("Invalid mark {} encountered. Exiting.".format(line.split()[0]))
    except ValueError:
        print("Invalid mark {} encountered. Exiting.".format(line.split()[0]))
    else:
        print("Best student: {}".format(best))

        print("Best mark: {}".format(highest))      


    # print("Best student: {}".format(best))

    # print("Best mark: {}".format(highest))

if __name__ == '__main__':
    main()


        

