import day13

if __name__ == "__main__":
    print("so. much. snow.")

    pattern = []

    with open("input_day14.txt") as input:
        for row in input:
            pattern.append(row.strip("\n"))
    
    print(pattern)
    # tilt north
    modifiedPattern = day13.transpose(pattern)
    print(modifiedPattern)
    # now north is to the left
    northTiltedPattern = []
    for row in modifiedPattern:
        row = list(row)
        prevWall = -1
        for index, char in enumerate(row):
            if char == "#":
                prevWall = index
            elif char == ".":
                # we do nothing?
                pass
            elif char == "O":
                # let's rollll
                if index > prevWall+1: # if the previous spot wasn't free, index = prevWall+1 -> no rolling
                    row[prevWall+1] = "O"
                    row[index] = "."
                    prevWall += 1
                else:
                    prevWall = index
        northTiltedPattern.append("".join(row))
    # put north back up north
    northTiltedPattern = day13.transpose(northTiltedPattern)
    # let's check
    print(northTiltedPattern)
    with open("stones.txt", "w") as file:
        for row in northTiltedPattern:
            file.write(row)
            file.write("\n")
    
    # count the load
    load = 0
    for index, row in enumerate(northTiltedPattern):
        weight = len(northTiltedPattern) - index
        for char in row:
            if char == "O":
                load += weight
    
    print(load)

                

    

