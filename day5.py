print("nice lil break coming up")

# converts the range; just hides some math; does not check range matches
def convertRange(rangeStart: int, rangeEnd: int, sourceStart: int, destinationStart: int)-> (int, int):
    newStart = destinationStart + rangeStart - sourceStart
    newEnd = destinationStart + rangeEnd - sourceStart
    return (newStart, newEnd)

with open ("input_day5.txt") as file:
    lines = file.readlines() # we get a list of strings

# okay now we have the contents, let's get to splitting eh
lines.reverse()

# first row has the seeds
row = lines.pop()
seeds = row.split(" ")[1:]

# this table has seven rows, one for each number type (seed, soil, fertilizer etc)
# each row is a table of all numbers in it
# each number is a tuple (rangeStart, rangeEnd)
importantNumbers = [[]] 

isSeed = True
thisSeed = -1
for seed in seeds:
    if isSeed:
        thisSeed = int(seed.strip())
        isSeed = False
    else:
        importantNumbers[0].append((thisSeed, (thisSeed + int(seed.strip()) - 1)))
        isSeed = True
    # this was for 1. solution importantNumbers[0].append(int(seed.strip()))

# next two lines we don't need (empty line + headline)
lines.pop()
lines.pop()

# make a list of decoding lists
decoders = [[]]
whichDecoder = 0 # index tells which decoder we are currently in

while lines:
    line = lines.pop()
    # print(line)
    if(line == "\n"): # encountered a change of maps
        lines.pop() # this is the headline line, we don't need that
        whichDecoder += 1 # move to the next decoder
        decoders.append([])
    else:
        values = line.split(" ")
        destinationStart = (int)(values[0].strip())
        sourceStart = (int)(values[1].strip())
        convertionRange = (int)(values[2].strip())
        decoders[whichDecoder].append((sourceStart, int(sourceStart+convertionRange - 1),destinationStart))

print(whichDecoder)
whichDecoder = 0
# now we have a list of decoders in the same order they appear in file
# each decoder: list of lists: [sourceStart, sourceEnd, destinationStart]

for typeDecoder in decoders:
    print("Decoder: "+ str(whichDecoder))
    print(importantNumbers[whichDecoder])
    importantNumbers.append([])
    while importantNumbers[whichDecoder]:
        # print(value)
        found = False
        rangeStart, rangeEnd = importantNumbers[whichDecoder].pop()
        for conversionInstruction in typeDecoder:
            """ this was for 1. part
            if (int(conversionInstruction[0]) <= int(value) <= int(conversionInstruction[1])):
                # found a match; lets make the conversion
                importantNumbers[whichDecoder+1].append(int(conversionInstruction[2] + (value - conversionInstruction[0])))
                found = True
                # print("found")
                break
        # if not found, add as is
        if not found:
            importantNumbers[whichDecoder+1].append(value)
            """
            # check if ranges overlap
            sourceStart, sourceEnd, destinationStart = conversionInstruction

            # completely inside, easypeasy:
            if (sourceStart <= rangeStart and rangeEnd <= sourceEnd):
                importantNumbers[whichDecoder+1].append(convertRange(rangeStart, rangeEnd, sourceStart, destinationStart))
                found = True
                break
            # overlaps partly
            else: 
                # range starts from earlier and has overlap
                if (rangeStart < sourceStart and sourceStart <= rangeEnd):
                    overlapStart = sourceStart
                    found = True
                else:
                    overlapStart = rangeStart
                # range ends later and has overlap
                if (rangeStart <= sourceEnd and sourceEnd < rangeEnd):
                    overlapEnd = sourceEnd
                    found = True
                else:
                    overlapEnd = rangeEnd

                # convert overlapping area and add the rest back to queue
                if found:
                    importantNumbers[whichDecoder+1].append(convertRange(overlapStart, overlapEnd, sourceStart, destinationStart))
                    if rangeStart < overlapStart:
                        importantNumbers[whichDecoder].append((rangeStart, overlapStart-1))
                    if rangeEnd > overlapEnd:
                        importantNumbers[whichDecoder].append((overlapEnd+1, rangeEnd))
                    break
        # found no mathches for this range, so it goes to the next list as is
        if not found:
            importantNumbers[whichDecoder+1].append((rangeStart, rangeEnd))

                    

    whichDecoder+=1
        
print("seeds:")        
print(importantNumbers[0])
print("locations: ")
locations = importantNumbers[7]
locations.sort()
print(locations)
print(locations[0])

# 69323689 is too high