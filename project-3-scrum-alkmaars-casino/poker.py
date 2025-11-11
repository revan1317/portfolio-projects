import random
import basis
import casino
from collections import Counter

# Variabelen voor de kaarten
vormen = ['♠', '♥', '♦', '♣']
getallen = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

#Saldo voor de ai-spelers
ai1_balans = 500
ai2_balans = 500

# Functie om een volledige stapel kaarten te genereren
def kaarten():
    return [{'vorm': vorm, 'getal': getal} for getal in getallen for vorm in vormen]


# Functie om een hand voor de dealer te delen
def hand_dealer(kaart, hoeveelheid_kaarten):
    return [kaart.pop(random.randint(0, len(kaart) - 1)) for _ in range(hoeveelheid_kaarten)]


# Functie om de hand van een speler te tonen
def hand_zien(hand, eigenaar="Hand"):
    print(f"{eigenaar}: " + " ".join([f"{kaartje['vorm']}{kaartje['getal']}" for kaartje in hand]))


# Functie om te kiezen hoeveel geld je wilt inzetten
def kies_inzet():
    import basis
    inzet = int(input(f"Je saldo: €{basis.balans}. Hoeveel wil je inzetten?(Type 0 om het spel te verlaten)\n"))
    if 1 <= inzet <= basis.balans:
        return inzet
    else:
        print(f"Ongeldige inzet. Voer een bedrag in tussen €1 en €{basis.balans}.")
    # If statement voor als je het spel wilt verlaten
    if inzet == 0:
        import basis
        basis.start()

def ai_actie(ai_balans, huidige_inzet):
    if ai_balans < huidige_inzet:
        print("🤖 AI foldt omdat hij niet genoeg geld heeft.")
        return "fold", 0
    elif random.random() < 0.2:
        raise_amount = min(ai_balans, huidige_inzet * 2)
        print(f"🤖 AI raised naar €{raise_amount}!")
        return "raise", raise_amount
    else:
        print("🤖 AI callt.")
        return "call", huidige_inzet


def call_fold_raise(huidige_inzet):
    while True:
        keuze = input(f"Wil je 'callen' (€{huidige_inzet}), 'folden' of 'raisen'? (c/f/r): ").lower()
        if keuze in ['c', 'call']:
            return "call", huidige_inzet
        elif keuze in ['f', 'fold']:
            return "fold", 0
        elif keuze in ['r', 'raise']:
            nieuwe_inzet = kies_inzet()
            return "raise", nieuwe_inzet
        else:
            print("Ongeldige keuze, typ 'c' om te callen, 'f' om te folden of 'r' om te raisen.")

# Functie om de pot te beheren
def pot_beheren(pot, inzet):
    pot += inzet
    print(f"💰 De pot bevat nu: €{pot}")
    return pot

# Functie om het spel te starten
def start():
    global ai1_balans, ai2_balans
    while basis.balans > 0 and ai1_balans > 0 and ai2_balans > 0:
        kaart = kaarten()
        random.shuffle(kaart)
# Zorgt ervoor dat de speler 2 kaarten krijgt en dat er 3 kaarten in het midden komen
        speler_hand = hand_dealer(kaart, 2)
        ai1_hand = hand_dealer(kaart, 2)
        ai2_hand = hand_dealer(kaart, 2)
        kaarten_op_de_tafel = hand_dealer(kaart, 3)
        
        pot = 0

        hand_zien(speler_hand, "Jouw hand:")
        hand_zien(kaarten_op_de_tafel, "Kaarten op tafel:")
        # Zorgt ervoor dat de inzet die gekozen wordt afgehaald van je saldo
        inzet = kies_inzet()
        basis.balans -= inzet
        pot = pot_beheren(pot, inzet)

        #Ai-spelers kunnen hun optie kiezen
        ai1_actie, ai1_inzet = ai_actie(ai1_balans, inzet)
        if ai1_actie != "fold":
            ai1_balans -= ai1_inzet
            pot = pot_beheren(pot, ai1_inzet)

        ai2_actie, ai2_inzet = ai_actie(ai2_balans, inzet)
        if ai2_actie != "fold":
            ai2_balans -= ai2_inzet
            pot = pot_beheren(pot, ai2_inzet)

        # Speler kiest actie (call, fold of raise)
        keuze, extra_inzet = call_fold_raise(inzet)

        if keuze == "fold":
            print("Je hebt gefold. Je verliest deze ronde. 😢")
            continue
        elif keuze == "raise":
            basis.balans -= extra_inzet
            pot = pot_beheren(pot, extra_inzet)

        # Als speler callt, worden er 2 extra kaarten op de tafel gelegd
        kaarten_op_de_tafel += hand_dealer(kaart, 2)
        hand_zien(kaarten_op_de_tafel, "Eindkaarten op tafel")

        #Willekeurige winnaar
        winnaar = random.choice(["speler", "ai1", "ai2"])
        if winnaar == "speler":
            print(f"🎉 Jij wint de ronde! Je ontvangt de pot van €{pot}.\nNiewe ronde is begonnen")
            basis.balans += pot
        elif winnaar == "ai1":
            print(f"🤖 AI 1 wint de pot van €{pot}.\nNiewe ronde is begonnen")
            ai1_balans += pot
        else:
            print(f"🤖 AI 2 wint de pot van €{pot}.\nNiewe ronde is begonnen")
            ai2_balans += pot

    print("Er is geen geld meer bij een van de spelers. Game over.")


start()
