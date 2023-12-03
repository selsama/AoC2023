print("Happy holidays")

with open("syote.txt") as tiedosto:

    kokoSumma = 0

    for rivi in tiedosto:
        eka = 0
        ekaloyty = False
        toka = 0
        merkkijono = ""
        for merkki in rivi:
            if merkki.isnumeric():
                if not ekaloyty:
                    eka = merkki
                    ekaloyty = True
                toka = merkki
                merkkijono = ""
            else:
                merkkijono += str(merkki)
                # print(merkkijono)
                pituus = len(merkkijono)
                numero = -1
                if pituus >= 3:
                    if "one" in merkkijono:
                        numero = 1
                    elif "two" in merkkijono:
                        numero = 2
                    elif "six" in merkkijono:
                        numero = 6
                if pituus >= 4:
                    if "four" in merkkijono:
                        numero = 4
                    elif "five" in merkkijono:
                        numero = 5
                    elif "nine" in merkkijono:
                        numero = 9
                if pituus >= 5:
                    if "three" in merkkijono:
                        numero = 3
                    elif "seven" in merkkijono:
                        numero = 7
                    elif "eight" in merkkijono:
                        numero = 8
                if numero != -1:
                    if not ekaloyty:
                        eka = numero
                        ekaloyty = True
                    toka = numero
                    merkkijono = merkki # Only the last character is needed for the future (as it might be the first character of another word)

        # print(eka, toka)
        luku = str(eka) + str(toka)
        print(luku)
        try:
            luku = int(luku)
            kokoSumma += luku
        except (Exception):
            print("ei ollu vissii lukui tms")
        
    print(kokoSumma)
