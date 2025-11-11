import casino
import random
import basis


def kies_inzet(): # Vraagt de speler om een inzet
    while True:
        try:
            inzet = int(input(f"Je saldo: €{basis.balans}. Hoeveel wil je inzetten?\n"))
            if inzet == 0: # Optie om het spel te verlaten
                print("Je hebt het spel verlaten")
                basis.start()
            elif 1 <= inzet <= basis.balans:
                return inzet
            print(f"Ongeldige inzet. Voer een bedrag in tussen €1 en €{basis.balans}.")
        except ValueError:
            print("Voer een geldig bedrag in.")


def draai_roulette():
    return random.randint(0, 36) # Willekeurig getal tussen 0 en 36


def bepaal_kleur(nummer): # Vergelijkt de getallen met de kleuren
    if nummer == 0:
        return 'groen'
    elif 1 <= nummer <= 10 or 19 <= nummer <= 28:
        return 'rood' if nummer % 2 != 0 else 'zwart'
    else:
        return 'zwart' if nummer % 2 != 0 else 'rood'


def vergelijk_gok(resultaat, gok): # Bepaalt of de gok correct is
    kleur = bepaal_kleur(resultaat)
    try:
        gok_nummer = int(gok)
        return gok_nummer == resultaat
    except ValueError:
        return gok.lower() == kleur


def hoofdprogramma(): # Print de main interface
    print("Welkom bij Roulette!")
    print("-----------------------------------")
    print("Zet in op een getal (0-36) of een kleur (rood/zwart/groen)")
    print("Typ '0' om het spel te verlaten.")
    print("-----------------------------------")

    while basis.balans > 0:
        inzet = kies_inzet() # Vraagt om een inzet
        gok = input("Op wat wil je inzetten? (getal/kleur): ").lower()

        input("Druk op Enter om het wiel te draaien...")
        resultaat = draai_roulette() # Genereert een willekeurig resultaat
        resultaat_kleur = bepaal_kleur(resultaat)
        print(f"De roulette kwam uit op: {resultaat} ({resultaat_kleur})")

        if vergelijk_gok(resultaat, gok): # Berekent winst volgens de roulette
            if gok.isdigit() and int(gok) == resultaat:
                winst = inzet * 35
            else:
                winst = inzet * 2 if resultaat != 0 else inzet * 35
            basis.balans += winst
            print(f"Gefeliciteerd! Je wint €{winst}!")
        else:
            basis.balans -= inzet
            print("Helaas, je hebt verloren.")

        print(f"Je nieuwe saldo is: €{basis.balans}") # Print het nieuwe saldo nadat je winst of verlies maakt

        if basis.balans <= 0: # Spel wordt gestopt zodra er geen saldo meer over is
            print("Je hebt geen saldo meer. Game over!")
            break


if __name__ == "__main__":
    hoofdprogramma()
