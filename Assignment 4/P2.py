import sys

def packageOptimize(values, sum):
    values.reverse()

    for item in values:
        if(sum % item == 0):
            print(sum // item)
            print(sum // item, "packages of size", item)
            exit(0)
    
    print("No solution found!")


def extractFile(fileName):
    file = open(fileName, "r+")
    lines = file.readlines()
    values = lines[0].split(",")

    sum = int(lines[1])
    return [int(x) for x in values], sum

values, sum = extractFile(str(sys.argv[1]))
packageOptimize(values, sum)