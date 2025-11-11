balans = 500


# start het programma en laat je kiezen wat je wil spelen
def start():
    schoonmaker()
    print(balans)
    spelkeuze = input("Welk spel wilt u spelen?\n1. Poker\n2. Roulette\n3. Black Jack\n4. Slots\nOf type '0' om het spel te sluiten\nsleuKeuze (1/2/3/4): ").lower()
    if spelkeuze == "1" or spelkeuze == "poker":  # stuurt je naar poker
        schoonmaker()
        import poker
        poker.start()
    elif spelkeuze == "2" or spelkeuze == "roulette":  # stuurt je naar roulette
        schoonmaker()
        import roulette
        roulette.hoofdprogramma()
    elif spelkeuze == "3" or spelkeuze == "black jack":  # stuurt je naar black jack
        schoonmaker()
        import black_jack
        black_jack.start()
    elif spelkeuze == "4" or spelkeuze == "slots":  # stuurt je naar slots
        schoonmaker()
        import slots
        slots.start()
    elif spelkeuze == "0" or spelkeuze == "exit":
        print("het spel sluit.")
        exit()
    else:
        print("dit spel ken ik niet controleer de spelling of gebruik de cijfers (1/2/3/4)")
        start()


# maakt het scherm leeg (in terminal)
def schoonmaker():
    import os
    import platform
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    return


if __name__ == "__main__":
    start()
