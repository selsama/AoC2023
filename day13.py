# import numpy

print("flu or not, time to code")

def isReflection(input:str, start:int):
    if start <=0 or start >= len(input):
        return False
    firsthalf = input[:start]
    lasthalf = input[len(input):(start-1):-1]
    if not len(firsthalf) == len(lasthalf):
        length = min(len(firsthalf), len(lasthalf))
        firsthalf = firsthalf[len(firsthalf)-length:]
        lasthalf = lasthalf[(len(lasthalf)-length):]
    # print(firsthalf)
    # print(lasthalf)
    if(firsthalf == lasthalf):
        return True
    return False

def findVerticalReflection(pattern:list, options:set=None) -> int:
    if not options:
        options = set(range(0,len(pattern[0])))
    for row in pattern:
        for i in range(len(row)):
            if i in options:
                if not isReflection(row,i):
                    options.remove(i)
                    # print("removed "+str(i))
        # did the row have points of reflection? if not, we ready
        # if multiple, keep checking next rows too
        if len(options) <= 0:
            return -1
    if len(options) == 1:
        return options.pop()
    else:
        return -1 # should never go here, but just in case

def transpose(pattern: list) -> list:
    transposedPattern = [""] * len(pattern[0])
    for row in pattern:
        for index, char in enumerate(row):
            transposedPattern[index] += char
    return transposedPattern

def findHorizontalReflection(pattern:list) -> int:
    return findVerticalReflection(transpose(pattern))

with open("input_day13.txt") as input:
    patterns = []
    index = 0
    patterns.append([])
    for row in input:
        if (len(row) <= 1):
            index += 1
            patterns.append([])
            continue
        patterns[index].append(row.strip('\n'))

sum = 0
splits = {} #index: v/h, splitSpot
index = 0


for pattern in patterns:
    columnsToLeft = findVerticalReflection(pattern)
    if columnsToLeft >0:
        sum += columnsToLeft
        print("index "+str(index)+": v, "+str(columnsToLeft))
    else:
        #flip the shit and check again
        rowsAbove = findHorizontalReflection(pattern)
        if rowsAbove > 0:
            sum += 100*rowsAbove
            print("index "+str(index)+": h, "+str(rowsAbove))
        else:
            print("this shouldn't have happened???")
    index += 1

print(sum)



