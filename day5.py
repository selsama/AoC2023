print("nice lil break coming up")

with open ("input_day5.txt") as file:
    lines = file.readlines() # we get a list of strings

# okay now we have the contents, let's get to splitting eh
lines.reverse()

# first row has the seeds
row = lines.pop()
seeds = row.split(" ")[1:]
importantNumbers = [[]]
for seed in seeds:
    importantNumbers[0].append(int(seed.strip()))

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
        decoders[whichDecoder].append([sourceStart, int(sourceStart+convertionRange),destinationStart])

print(whichDecoder)
whichDecoder = 0
# now we have a list of decoders in the same order they appear in file
# each decoder: list of lists: [sourceStart, sourceEnd, destinationStart]

for typeDecoder in decoders:
    # print(whichDecoder)
    # print(importantNumbers)
    importantNumbers.append([])
    for value in importantNumbers[whichDecoder]:
        # print(value)
        found = False
        for conversionInstruction in typeDecoder:
            if (int(conversionInstruction[0]) <= int(value) <= int(conversionInstruction[1])):
                # found a match; lets make the conversion
                importantNumbers[whichDecoder+1].append(int(conversionInstruction[2] + (value - conversionInstruction[0])))
                found = True
                # print("found")
                break
        # if not found, add as is
        if not found:
            importantNumbers[whichDecoder+1].append(value)
    whichDecoder+=1
        
print("seeds:")        
print(importantNumbers[0])
print("locations: ")
locations = importantNumbers[7]
locations.sort()
print(locations[0])


    