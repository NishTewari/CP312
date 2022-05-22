import sys
#testfile = "testfile.txt"

def maxValueSeq(values, p, n):
    values.sort()
    sum = 0
    maxValSeq = []
    for item in values:
        # Negative Values
        if (n > 0):
            sum -= item
            maxValSeq.append("-")
            n-=1
            maxValSeq.append(item)
        
        # Postive Values
        else:
            sum += item
            maxValSeq.append("+")
            p-=1
            maxValSeq.append(item)

    return sum, maxValSeq


def processFile(fileName):
    file = open(fileName, "r+")
    lines = file.readlines()
    values = lines[0].strip().split(",")
    p = int(lines[1].strip())
    n = int(lines[2].strip())

    return [int(x) for x in values], p, n

values, p, n = processFile(str(sys.argv[1]))
sum, maxValSeq = maxValueSeq(values, p, n)

valueOutput = ""
for i in maxValSeq:
    valueOutput += str(i)
    valueOutput += " "
valueOutput += "= "
valueOutput += str(sum)

print(sum)
print(valueOutput)