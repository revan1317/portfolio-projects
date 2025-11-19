def bereken_eieren(portiegrootte):
    return portiegrootte * (1 / 4)

def bereken_boter(portiegrootte):
    return portiegrootte * (60 / 4)

def bereken_suiker(portiegrootte):
    return portiegrootte * (50 / 4)

def bereken_bloem(portiegrootte):
    return portiegrootte * (55 / 4)

def combineer(portiegrootte):
    eieren = bereken_eieren(portiegrootte)
    boter = bereken_boter(portiegrootte)
    suiker = bereken_suiker(portiegrootte)
    bloem = bereken_bloem(portiegrootte)
    return eieren, boter, suiker, bloem

porties = [12, 24, 52]

totaal_eieren = 0
totaal_boter = 0
totaal_suiker = 0
totaal_bloem = 0

for portie in porties:
    portie_eieren, portie_boter, portie_suiker, portie_bloem = combineer(portie)
    print(f"Voor een portie van {portie} heb ik {int(portie_eieren)} eieren, {portie_boter:.1f}g boter, {portie_suiker:.1f}g suiker, {portie_bloem:.1f}g bloem nodig.")

    totaal_eieren += portie_eieren
    totaal_boter += portie_boter
    totaal_suiker += portie_suiker
    totaal_bloem += portie_bloem

print(f"\nIn totaal heb ik {int(totaal_eieren)} eieren, {totaal_boter:.1f}g boter, {totaal_suiker:.1f}g suiker, {totaal_bloem:.1f}g bloem nodig.")
