stemd = 0
stemz = 0

while True:
    stem = input("Op wie wil je stemmen?").lower()
    if stem == "uitslag":
        break
    if stem == "dominique":
        stemd += 1
    elif stem == "zacharia":
        stemz += 1
    else:
        print("Ongeldige keuze")



if stemd > stemz:
    print("Dominique heeft gewonnen!")
elif stemz > stemd:
    print("Zacharia heeft gewonnen!")
else:
    print("Dominque en Zacharia hebben een gelijk aantal stemmen")
