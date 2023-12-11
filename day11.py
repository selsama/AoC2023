print("allright time for a bit of a space adventure")

with open("input_day11.txt") as input:
    emptyRows = 0
    galaxies = []
    for iY, line in enumerate(input):
        rowIsEmpty = True
        for iX, char in enumerate(line):
            if char == "#":
                rowIsEmpty = False
                galaxies.append([iY+emptyRows,iX])
        if rowIsEmpty:
            emptyRows +=(1000000-1)

# okay so now we have the locations of the galaxies: y-loc is right, x-loc still unexpanded
# let's expand the x

galaxies.sort(key = lambda x: x[1])

print(galaxies)

previous = 0
expandedGalaxies = []*len(galaxies)
emptyColumns = 0
for galaxy in galaxies:
    if galaxy[1] - previous > 1:
        emptyInBetween = ((galaxy[1] - previous) -1)
        emptyInBetween *= (1000000-1)
        emptyColumns += emptyInBetween
    expandedGalaxies.append([galaxy[0],galaxy[1]+emptyColumns])
    previous = galaxy[1]


print("\n")
print(expandedGalaxies)

# ok seems to do the expansion just fine as it should
# then to the question

distances = []
for intY in range(0,len(expandedGalaxies)):
    distances.append([])
    for intX in range(0,len(expandedGalaxies)):
        distanceX = abs(expandedGalaxies[intY][1] - expandedGalaxies[intX][1])
        distanceY = abs(expandedGalaxies[intY][0] - expandedGalaxies[intX][0])
        distances[intY].append(distanceX+distanceY)

#print(distances)
sum=0
for row in distances:
    for num in row:
        if num == 0:
            break
        else:
            sum += num

print(sum)

# 4477369088302 too high: i think one extra per column let's see
# 447745088302 still too high (as yeah you'd think there'd be bigger difference ugh let's think this through)
# 447744640566
# ...... or maybe MAYBE it would help to read the instructions (1 million vs 10 million.....)