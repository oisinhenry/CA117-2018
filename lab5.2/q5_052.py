
import sys
def main():

    names = []

    skipped = []
    students = {}
    for line in sys.stdin:
        line = line.replace("," , " ")
        line = line.strip().split(":")
        marks = line[1]
        marks = marks.strip().split()
        for i in range(0 , len(marks)):
            try:
                marks[i] = int(marks[i])
            except:
                pass
        try:
            students[line[0]] = sum(marks)
        except:
            skipped.append(line[0])
            pass

    

    for keys , values in sorted(students.items() , key = lambda x: x[1] , reverse = True):
        print('{} : {}'.format(keys , values))
    print("Skipped:")
    for i in range(0 , len(skipped)):
        #print("Skipped:")
        print(skipped[i])







    



if __name__ == '__main__':
    main()