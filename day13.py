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
    return mismatches(firsthalf, lasthalf)


def mismatches(first:str, second:str) -> int:
    mismatches = 0
    for i in range(0,len(first)):
        if not first[i] == second[i]:
            mismatches +=1
        if mismatches > 1:
            return 2
    return mismatches


def findVerticalReflection(pattern:list) -> int:
    options = dict.fromkeys(range(len(pattern[0])),False)
    for row in pattern:
        for i in range(len(row)):
            if i in options:
                mismatches = isReflection(row,i)
                if mismatches == 2:
                    del options[i]
                elif mismatches == 1:
                    if options[i]: # already had a smudge, can't have more
                        del options[i]
                    else:
                        options[i] = True # first smudge, so is fine
        # did the row have points of reflection? if not, we ready
        # if multiple, keep checking next rows too
        if len(options) <= 0:
            return -1
    for key in options:
        if options[key]: # found exactly one smudge
            return key
    return -1 # only found the og line i guess

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



