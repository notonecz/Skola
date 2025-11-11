print("Převodník")

den = int(input("Zadejte pořadové číslo dne: "))

if 1 <= den <= 7:
    if den == 1:
        print("Pondělí")
    elif den == 2:
        print("Úterý")
    elif den == 3:
        print("Středa")
    elif den == 4:
        print("Čtvrtek")
    elif den == 5:
        print("Pátek")
    elif den == 6:
        print("Sobota")
    elif den == 7:
        print("Neděle")
else:
    print("Neplatný den")

mesic = int(input("Zadejte pořadové číslo měsíce: "))

if 1 <= mesic <= 12:

    print()

    if 3 <= mesic <= 5:

        if mesic == 3:
            print("Březen")
        elif mesic == 4:
            print("Duben")
        elif mesic == 5:
            print("Květen")

        print("Jarní měsíc")
    elif 6 <= mesic <= 8:

        if mesic == 6:
            print("Červen")
        elif mesic == 7:
            print("Červenec")
        elif mesic == 8:
            print("Srpen")

        print("Letní měsíc")
    elif 9 <= mesic <= 11:

        if mesic == 9:
            print("Září")
        elif mesic == 10:
            print("Říjen")
        elif mesic == 11:
            print("Listopad")

        print("Podzminí měsíc")

    elif 1 <= mesic <= 2 or mesic == 12:

        if mesic == 1:
            print("Leden")
        elif mesic == 2:
            print("Únor")
        elif mesic == 12:
            print("Prosinec")

        print("Zimní měsíc")

    if 1 <= mesic <= 6:
        print("První pololetí")

    elif 7 <= mesic <= 12:
        print("Druhe pololetí")

else:
    print("Neplatný měsíc")
