import math

print("Happy independence day!")

# input = [(38,241), (94,1549), (79,1074), (70,1091)]
# input = [(7,9), (15,40), (30,200)]
input = [(38947970,241154910741091)]


# speed = timeHeld
# distance = remainingTime * speed
# distance = remainingTime * timeHeld
# totalTime = timeHeld + remainingTime
# distance = (totalTime - timeHeld) * timeHeld 

# when is distance (counted) > record?
# find zero
# totalTime*timeheld - timeheld^2 - record = 0
# timeHeld = -totalTime +- sqrt(totalTime^2-4*(-1)*(-record))
#            ------------------------------------------------
#                         2*(-1)

noOfWays = 1

for pair in input:
    totalTime, record = pair
    totalTime = float(totalTime)
    record = float(record)
    root = math.sqrt(totalTime*totalTime-(4*(-1)*(-record)))
    solution1 = (-totalTime + root)/float(-2)
    solution2 = (-totalTime-root)/float(-2)
    # print(solution1)
    # print(solution2)
    # jos ei jakojäännöstä:
    if (solution2 % int(solution2)== 0):
        solution2 -= 1

    options = int(solution2) - int(solution1)
    print(options)
    # noOfWays *= options
# the best options are always in the middle (cuz we can't win by not holding or not letting go)

# print(noOfWays)