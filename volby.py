x = int(input("Zadej x: "))
y = int(input("Zadej y: "))
z = int(input("Zadej z: "))

xSude = x % 2 == 0
ySude = y % 2 == 0
zSude = z % 2 == 0

xLiche = not xSude
yLiche = not ySude
zLiche = not zSude

if (xSude + ySude + zSude) == 1 and (x+y+z) % 3 == 0:
    print("Vládnou Lichouni!")
elif (x > 2 or y > 2 or z > 2) and xSude and ySude and zSude:
    print("Vládnou Sudáci!")
elif (0 <= x and 0 <= y and 0 <= z) and (x > 100 or y > 100 or z > 100):
    print("Vládnou Velikáni!")
else:
    print("Vládne Pan Minus!")