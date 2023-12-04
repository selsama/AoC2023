print("just another manic Monday")

with open("syote_day4.txt") as file:
    totalPoints = 0

    for row in file:
        nros = row.split(":")[1]
        winners = nros.split("|")[0].split(" ")
        myNros = nros.split("|")[1].split(" ")

        rowPoints = 0
        firstFound = False
        for number in myNros:
            number = number.strip()
            if number not in winners:
                continue
            try:
                int(number)
                if not firstFound:
                    firstFound = True
                    rowPoints = 1
                    # print(number + " is the first")
                else:
                    rowPoints *= 2
                    # print(rowPoints)
            except:
                # print(number + " is not a number")
                pass
        
        totalPoints += rowPoints


    print(totalPoints)
