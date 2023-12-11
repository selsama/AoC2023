import sys

sys.setrecursionlimit(20000)

print("yeah forget it i'm not gonna do another candle pic")

with open("input_day10.txt") as input:
    indexY = -1
    map = []
    secondMap = []
    startPoint = (-1,-1)
    for line in input:
        indexY += 1
        map.append([])
        secondMap.append([])
        indexX = -1
        for char in line:
            indexX += 1
            if (char == "\n"):
                continue
            map[indexY].append(char)
            secondMap[indexY].append(" ")
            if (char == "S"):
                startPoint = (indexY, indexX)

stepCount = 0

# okay so now we have the input mapped
# let's find the loop

# starting from s, let's go N, E, S, W as needed

# moving: check connection; either back to start or count steps & move on

# oh yeaf this stuff should be in a main block or smth
# ehh whatevs



def goNorth(iY,iX) -> next:
    # print("N")
    global stepCount
    stepCount += 1
    markPotentials(iY,iX)
    if(iY <= 0):
        found = False
    elif(map[iY-1][iX] == "S"):
        found = True
    elif(map[iY-1][iX] not in ["|", "7", "F"]):
        found = False
    elif(map[iY-1][iX] == "|"): # next up to north again
        found = goNorth(iY-1, iX)
    elif(map[iY-1][iX] == "7"):
        found = goWest(iY-1, iX)
    else:
        found = goEast(iY-1, iX)
    if not found:
        stepCount -=1
    return found
    
def goSouth(iY, iX) -> next:
    #print("S")
    global stepCount
    stepCount += 1
    markPotentials(iY,iX)
    if(iY>= 140):
        found = False #out of bounds
    elif(map[iY+1][iX] == "S"):
        found = True
    elif(map[iY+1][iX] not in ["|", "L", "J"]):
        found = False #does not connect
    elif(map[iY+1][iX] == "|"):
        found = goSouth(iY+1, iX)
    elif(map[iY+1][iX] == "L"):
        found = goEast(iY+1, iX)
    else:
        found = goWest(iY+1, iX)
    if not found:
        stepCount -=1
    return found

def goEast(iY, iX) -> next:
    #print("E")
    global stepCount
    stepCount += 1
    markPotentials(iY,iX)
    if(iX >= 140):
        found = False
    elif(map[iY][iX+1] == "S"):
        found = True
    elif(map[iY][iX+1] not in ["-", "J", "7"]):
        found = False
    elif(map[iY][iX+1] == "-"):
        found = goEast(iY, iX+1)
    elif(map[iY][iX+1] == "J"):
        found = goNorth(iY, iX+1)
    else:
        found = goSouth(iY, iX+1)
    if not found:
        stepCount -=1
    return found

def goWest(iY,iX) -> next:
    #print("W")
    global stepCount
    stepCount += 1
    markPotentials(iY,iX)
    if(iX <= 0):
        found = False
    elif(map[iY][iX-1] == "S"):
        found = True
    elif(map[iY][iX-1] not in ["-", "L", "F"]):
        found = False
    elif(map[iY][iX-1] == "-"):
        found = goWest(iY, iX-1)
    elif(map[iY][iX-1] == "L"):
        found = goNorth(iY, iX-1)
    else:
        found = goSouth(iY, iX-1)
    if not found:
        stepCount -=1
    return found

def markPotentials(iY,iX):
    global secondMap
    global map
    secondMap[iY][iX] = map[iY][iX]
    '''
    if not iY <= 1:
        if not map[iY-1][iX] == "*":
            secondMap[iY-1][iX] = "+"
    if not iY >= 139:
        if not map[iY+1][iX] == "*":
            secondMap[iY+1][iX] == "+"
    if not iX <= 1:
        if not map[iY][iX-1] == "*":
            secondMap[iY][iX-1] = "+"
    if not iX >= 139:
        if not map[iY][iX+1] == "*":
            secondMap[iY][iX+1] = "+"
    '''


print(startPoint)

'''
if(goNorth(startPoint[0], startPoint[1])):
    print("went north coolio")
    print(stepCount)
elif(goEast(startPoint[0],startPoint[1])):
    print("went east coolio")
    print(stepCount)
else:
    goSouth(startPoint[0], startPoint[1])
    print("went south coolio")
    print(stepCount)
'''

# part two: now we already know which way
# let's fill in where the pipes that belong are
print(goSouth(startPoint[0], startPoint[1]))
print(stepCount)
# check how many are surrounded

surrounded = 0
candidates = set()


# seems that the following idea was right but for some reason I couldn't get it debugged (at 4am), so rewrite below
'''
for y in range(0,140): #check only taking into account rows
    started = False
    previous = None
    for x in range(0,140):
        if not secondMap[y][x] == " ":
            if secondMap[y][x] == "-":
                continue
            elif secondMap[y][x] == "|":
                started = not started
                continue
            if previous: # these pairings change, others keep the same
                if (previous and secondMap[y][x]) in ("7","S","F"):
                    started = not started
                elif (previous and secondMap[y][x]) in ("J", "L"):
                    started = not started
                previous = None
            else:
                previous = secondMap[y][x]
        else: # if not part of the main pipe, might be inside
            if started:
                candidates.add((y,x))

# now candidates only contain those that could be inside based on the row config only, next check columns
for x in range(0,140):
    started = False
    previous = None
    for y in range(0,140):
        if not secondMap[y][x] == " ":
            if secondMap[y][x] == "|": 
                continue
            elif secondMap[y][x] == "-":
                started = not started
                continue
            if previous:
                if (previous and secondMap[y][x]) in ("7","S","L"):
                    started = not started
                elif (previous and secondMap[y][x]) in ("J", "F"):
                    started = not started
                previous = None
            else:
                previous = secondMap[y][x]   
        else:
            if started:
                if (y,x) in candidates:
                    surrounded += 1


'''

inside = False
pipeStart = None


for indexY, row in enumerate(secondMap):
    for indexX, char in enumerate(row):
        if char == " ":
            if inside:
                candidates.add((indexY,indexX))
        else: # tile is part of the main loop
            if char == ("F") or char ==("L"):
                if pipeStart:
                    print("Pipe shouldn't have started")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
                else:
                    pipeStart=char
            elif char == "7" or char == "S":
                if pipeStart == ("F"):
                    inside = inside
                    pipeStart = None
                elif pipeStart == "L":
                    inside = not inside
                    pipeStart = None
                else:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
            elif char == "J":
                if pipeStart == ("F"):
                    inside = not inside
                    pipeStart = None
                elif pipeStart == "L":
                    inside = inside
                    pipeStart = None
                else:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
            elif char == "-":
                if pipeStart:
                    continue
                else:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
            elif char == "|":
                if pipeStart:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
                else:
                    inside = not inside
            else:
                print("how tf")
                print(str(indexY)+", "+str(indexX)+" ("+char+")")

for indexX in range(len(secondMap)):
    for indexY in range(len(secondMap)):
        char = secondMap[indexY][indexX]
        if char == " ":
            if inside:
                if (indexY,indexX) in candidates:
                    print(str(indexY)+", "+str(indexX)+" ("+char+") is in!")
                    surrounded += 1
                else:
                    print(str(indexY)+", "+str(indexX)+" ("+char+") is not in row-wise")

        else: # tile is part of the main loop
            if char == "7" or char == "F" or char == "S":
                if pipeStart:
                    print("Pipe shouldn't have started")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
                else:
                    pipeStart=char
            elif char ==  "J":
                if pipeStart == "7" or pipeStart == "S":
                    inside = inside
                    pipeStart = None
                elif pipeStart == "F":
                    inside = not inside
                    pipeStart = None
                else:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
            elif char == "L":
                if pipeStart == "7" or pipeStart == "S":
                    inside = not inside
                    pipeStart = None
                elif pipeStart == "F":
                    inside = inside
                    pipeStart = None
                else:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
            elif char == "|":
                if pipeStart:
                    continue
                else:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
            elif char == "-":
                if pipeStart:
                    print("pipe broken")
                    print(str(indexY)+", "+str(indexX)+" ("+char+")")
                else:
                    inside = not inside
            else:
                print("how tf")
                print(str(indexY)+", "+str(indexX)+" ("+char+")")
                





print(candidates)
print(surrounded)


with open("pipemap.txt", "w") as file:
    for line in secondMap:
        for char in line:
            file.write(char)
        file.write("\n")

# 1141 too high
# 398 still too high
# 291 was correct