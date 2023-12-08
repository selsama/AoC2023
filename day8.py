print("I saw the crescent; You saw the whole of the moon")

from collections import deque
import math

with open("input_day8.txt") as file:
    instructionLine = file.readline()
    directions = deque()
    for character in instructionLine:
        if (character == "L"):
            directions.append(0)
        elif (character == "R"):
            directions.append(1)
    
    # instructions are ready; now skip the empty line
    file.readline()
    
    # now to build a hashmap
    map = {}

    # and for part 2, list of start/end nodes
    startNodes = []
    currentNodes = []
    endNodes = set()

    line = file.readline()
    while (line != ""):
        node = line[0:3]
        left = line[7:10]
        right = line[12:15]

        map[node] = (left,right)

        # see if this is a start/end node
        if (node[2] == "A"):
            startNodes.append(node)
            currentNodes.append(node)
        elif (node[2] == "Z"):
            endNodes.add(node)

        line = file.readline()
    
    # ok then follow instructions till we get to zzz

    steps = 0

    # 1. part
    '''
    node = "AAA"

    print(node)

    while (node != "ZZZ"):
        dir = directions.popleft()
        node = map.get(node)[dir]
        steps += 1
        directions.append(dir)
    '''
        
    areWeThereYet = False
    print(startNodes)
    print(endNodes)



    # 2. part
    ''' FINE i'll figure out a faster way then ffs
    But considering the question, you'd KINDA THINK it'd ALSO be noteworthy as to HOW we got there so yahh
    while not areWeThereYet:
        # print(currentNodes)
        areWeThereYet = True
        dir = directions.popleft()
        for index in range(3):
            next = map.get(currentNodes[index])[dir]
            if next not in endNodes:
                areWeThereYet = False
            currentNodes[index] = next
        steps += 1
        directions.append(dir)
        
        if(steps%1000000==0):
            print(steps)
        if steps > 58450000:
            break
    '''


    print(steps)
    loops = []
    index = 0
    loopLengths = []

    for node in currentNodes:
        myDirections = directions.copy()
        start = node
        steps = 0
        beenTo = {}
        print(beenTo)
        while not beenTo.get(node): #let's look for any loops
            if node in endNodes:
                beenTo[node] = steps
            if node in startNodes:
                beenTo[node] = steps
            dir = myDirections.popleft()
            node = map.get(node)[dir]
            steps += 1
            myDirections.append(dir)
        end = node
        loopLength = steps - beenTo.get(node)
        loopLengths.append(loopLength)
        loops.append((start,end,loopLength,beenTo))

    for line in loops:
        print(line)
        print("\n")

    # we need to fine x where x % loopLength for each of the starts equals 0
    # that is, find the least common multiple
    # and would you look at that


    print(math.lcm(*loopLengths))

        


