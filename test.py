print("Převodník")

den = int(input("Zadejte pořadové číslo dne: "))

if 1 <= den <= 7:
    if den == 1:
        print("Pondělí")
    if den == 2:
        print("Úterý")
    if den == 3:
        print("Středa")
    if den == 4:
        print("Čtvrtek")
    if den == 5:
        print("Pátek")
    if den == 6:
        print("Sobota")
    if den == 7:
        print("Neděle")
else:
    print("Neplatný den")

mesic = int(input("Zadejte pořadové číslo měsíce: "))

if 1 <= mesic <= 12:

    print()

    if 3 <= mesic <= 5:

        if mesic == 3:
            print("Březen")
        if mesic == 4:
            print("Duben")
        if mesic == 5:
            print("Květen")

        print("Jarní měsíc")
    if 6 <= mesic <= 8:

        if mesic == 6:
            print("Červen")
        if mesic == 7:
            print("Červenec")
        if mesic == 8:
            print("Srpen")

        print("Letní měsíc")
    if 9 <= mesic <= 11:

        if mesic == 9:
            print("Září")
        if mesic == 10:
            print("Říjen")
        if mesic == 11:
            print("Listopad")

        print("Podzminí měsíc")
    if 1 <= mesic <= 2 or mesic == 12:

        if mesic == 1:
            print("Leden")
        if mesic == 2:
            print("Únor")
        if mesic == 12:
            print("Prosinec")

        print("Zimní měsíc")
else:
    print("Neplatný měsíc")
