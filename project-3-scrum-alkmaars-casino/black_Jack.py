from plaatjes_slots import printer as printer
import basis
# naam = [status, total]
speler = 0
huis = [0, 0]
NPC1 = [0, 0]
NPC2 = [0, 0]


def hit():
    import random
    return random.randint(1, 11)


def spelerprofiel():
    global speler
    if speler > 21:
        print(f"Je heb {speler} en verliest")
        start()
    elif speler == 21:
        input("Je wint met 21!! (+€100)\n\ndruk op enter om terug te gaan:")
        basis.balans += 100
        start()
    print(f"Je heb {speler}")
    return


def huisprofiel():
    global huis
    NPC1[1] += hit()
    if huis[1] > 21:
        huis[0] = 1
        print(f"Huis heeft {huis[1]} en verliest")
        return
    elif huis[1] == 21:
        input("huis wint met 21!!\ninzet verloren\n\ndruk op enter om terug te gaan:")
        start()
    print(f"huis heeft {huis[1]}")
    return


def npc1profiel():
    global NPC1
    NPC1[1] += hit()
    if NPC1[1] > 21:
        NPC1[0] = 1
        print(f"NPC1 heeft {NPC1[1]} en verliest")
        return
    elif NPC1[1] == 21:
        input("NPC1 wint met 21!!\ninzet verloren\n\ndruk op enter om terug te gaan:")
        start()
    print(f"NPC1 heeft {NPC1[1]}")
    return


def npc2profiel():
    global NPC2
    NPC1[1] += hit()
    if NPC2[1] > 21:
        NPC2[0] = 1
        print(f"NPC2 heeft {NPC2[1]} en verliest")
        return
    elif NPC2[1] == 21:
        input("NPC2 wint met 21!!\ninzet verloren\n\ndruk op enter om terug te gaan:")
        start()
    print(f"npc2 heeft {NPC2[1]}")
    return


def spel():
    global huis, speler, NPC1, NPC2
    basis.schoonmaker()
    print(basis.balans)

    if huis[0] == 0:
        huisprofiel()

    hitkeuze = input(f"je hand = {speler}\nzeg 'hit' voor een extra kaart of zeg niets om verder te gaan: ").lower()
    if hitkeuze == "hit":
        NPC2[1] += hit()
    spelerprofiel()

    if NPC1[0] == 0:
        npc1profiel()
    if NPC2[0] == 0:
        npc2profiel()


def opstarter():
    # geeft de start handen
    global huis, speler, NPC1, NPC2
    speler = hit() + hit()
    huis = [0, hit() + hit()]
    NPC1 = [0, hit() + hit()]
    NPC2 = [0, hit() + hit()]

    if speler == 21:
        basis.schoonmaker()
        input("21!!!!\nje wint meteen: (enter)")
        basis.balans += 200
        start()
    # start spel
    spel()


def start():
    print(basis.balans)
    printer.kiesprint('7')
    keuze = input("Druk op enter om te beginnen of type 'exit' om te stoppen\nSpeel NU! (-€50):")
    basis.balans -= 50

    # sluit spel
    if keuze == 'exit':
        basis.start()
    opstarter()


start()
