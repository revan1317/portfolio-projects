import random

def speel_ronde(chips):
    inzetten = []

    while chips > 0:
        print(f"\nJe hebt {chips} chips over.")
        invoer = input("Op welk nummer wil je inzetten? (0-36), of typ 'STOP' om te stoppen: ")

        if invoer.upper() == "STOP":
            break

        try:
            nummer = int(invoer)
            if nummer < 0 or nummer > 36:
                print("Voer een geldig nummer in (tussen 0 en 36).")
                continue

            chips -= 1
            inzetten.append(nummer)
            print(f"Je hebt 1 chip ingezet op nummer {nummer}.")

            if chips == 0:
                print("Je hebt al je chips ingezet. Rien ne va plus!")
                break

        except ValueError:
            print("Voer een geldig nummer in (tussen 0 en 36).")

    if chips <= 0 and not inzetten:
        print("\nJe hebt geen chips meer over. GAME OVER!")
        return chips, False

    print("\nRien ne va plus! De roulette draait...")
    winnend_nummer = random.randint(0, 36)
    print(f"Het winnende nummer is: {winnend_nummer}")

    winst = inzetten.count(winnend_nummer) * 35
    if winst > 0:
        chips += winst
        print(f"Gefeliciteerd! Je hebt {winst} chips gewonnen!")
    else:
        print("Helaas, je hebt deze ronde niet gewonnen.")

    print(f"Je nieuwe saldo is {chips} chips.")
    return chips, True

def start_spel():
    chips = 10
    print("Welkom bij de roulettetafel! Je start met 10 chips.")

    while chips > 0:
        chips, doorgaan = speel_ronde(chips)
        if not doorgaan:
            break

    print("\nBedankt voor het spelen! Tot de volgende keer.")

start_spel()
