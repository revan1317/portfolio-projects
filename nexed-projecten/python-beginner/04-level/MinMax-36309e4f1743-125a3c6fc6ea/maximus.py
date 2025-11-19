lijst = [3, 7, 10, 40, 2, 4, 8]
grootste = lijst[0]

for getal in lijst:
    if getal > grootste:
        grootste = getal

print(grootste)
