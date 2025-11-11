def print_welkom():
    # Welkoms bericht met ASCII art
    welkom_art = r"""
 __        __   _                               
 \ \      / /__| | ___ ___  _ __ ___   ___ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ |
   \ V  V /  __/ | (_| (_) | | | | | |  __/
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
    """
    print(welkom_art)


def print_gewonnen():
    # ASCII art om te laten zien dat de speler gewonnen heeft
    gewonnen_art = r"""
/  _____/  ______  _  ______   ____   ____   ____   ____  
/   \  ____/ __ \ \/ \/ /  _ \ /    \ /    \_/ __ \ /    \ 
\    \_\  \  ___/\     (  <_> )   |  \   |  \  ___/|   |  |
 \______  /\___  >\/\_/ \____/|___|  /___|  /\___  >___|  /
        \/     \/                  \/     \/     \/     \/
    """
    print(gewonnen_art)


def john_pork_pad():
    # Speler kiest voor John Pork pad en er breekt een gevecht uit
    print("Je hebt John Pork gekozen! Er begint een gevecht.")
    print("Kies je wapen: 'boog' of 'zwaard'")
    wapen = input("> ").lower()

    # Afhankelijk van het wapen dat je kiest, wint of verliest de speler het gevecht
    if wapen == "boog":
        print("Je gebruikt een boog en wint het gevecht!")
        print("Je verslaat John Pork en gaat naar het vliegveld.")
        vliegveld_keuze()
    elif wapen == "zwaard":
        print("Je kiest het zwaard, maar verliest het gevecht.")
        print("Game Over.")
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        john_pork_pad()


def chill_guy_pad():
    # De speler kiest ervoor om Chill Guy te volgen maar dit leidt tot de dood
    print("Je hebt gekozen om Chill Guy te volgen...")
    print("Helaas vertrouwt Chill Guy je niet en vermoordt hij je.")
    print("Game Over.")


def mexico_verhaal():
    # De speler komt aan in mexico en ontmoet el chapo
    print("Je komt aan in Mexico en ontmoet El Chapo.")
    print("El Chapo vraagt of je zijn vriend wilt worden.")
    vriend_keuze = input("Wil je vrienden worden met El Chapo? (ja/nee): ").lower()

    if vriend_keuze == "nee":
        # Speler wordt doodgeschoten en verliest
        print("Een van El Chapo's gangleden schiet je neer.")
        print("Game Over.")
        return
    elif vriend_keuze == "ja":
        # Speler wordt gepromoveerd tot drugsbaas en krijgt een opdracht
        print("El Chapo is blij met je keuze en promoveert je tot drugsbaas.")
        print("El Chapo geeft je een opdracht: start een gangoorlog met een rivaliserende gang.")
        oorlog_keuze = input("Wil je een gangoorlog starten? (ja/nee): ").lower()

        if oorlog_keuze == "nee":
            # Speler weigert en wordt opgepakt
            print("Je weigert de opdracht en wordt opgepakt door de autoriteiten.")
            print("Je wordt opgesloten en verliest de game.")
            return
        elif oorlog_keuze == "ja":
            # Speler start de oorlog en moet een aanval kiezen
            print("Er breekt een gangoorlog uit.")
            print("Je moet kiezen waar je de aanval wilt inzetten: noorden of zuiden.")
            aanval_keuze = input("Kies je aanvalsrichting (noorden/zuiden): ").lower()

            if aanval_keuze == "noorden":
                # Speler verliest de oorlog
                print("Je troepen worden overspoeld door de vijand en je verliest het gevecht.")
                print("Game Over.")
                return
            elif aanval_keuze == "zuiden":
                # Speler wint de oorlog en wordt gepromoveerd
                print("Je wint het gevecht en El Chapo promoveert je tot president van de cartel.")
                print("Plotseling kom je John Pork tegen.")
                print("John Pork richt een pistool op je en jij richt ook een pistool op hem.")
                schiet_keuze = input("Schiet je John Pork dood? (ja/nee): ").lower()

                if schiet_keuze == "nee":
                    print("John Pork schiet je dood.")
                    print("Game Over.")
                    return
                elif schiet_keuze == "ja":
                    # Speler wint de game
                    print("Je schiet John Pork dood en wint het spel!")
                    print_gewonnen()
                    return
                else:
                    print("Ongeldige keuze. Probeer opnieuw.")
                    mexico_verhaal()
            else:
                print("Ongeldige keuze. Probeer opnieuw.")
                mexico_verhaal()
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
            mexico_verhaal()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        mexico_verhaal()


def japan_verhaal():
    # Speler komt aan in Japan en ontmoet een mysterieuze man
    print("Je komt aan in Japan en ontmoet een vreemde, mysterieuze man.")
    print("Hij vraagt of je met hem mee wilt gaan naar een geheime locatie.")
    keuze = input("Ga je mee? (ja/nee): ").lower()

    while True:
        if keuze == "nee":
            print("Weet je het zeker?")
            zeker_keuze = input("Weet je zeker dat je niet mee wilt gaan? (ja/nee): ").lower()
            if zeker_keuze == "ja":
                # Speler wordt ontvoerd en vermoord
                print("Je wordt ontvoerd door een groep mannen met demonische maskers.")
                print("Ze brengen je naar een afgelegen plek en schieten je dood.")
                print("Game Over.")
                return
            elif zeker_keuze == "nee":
                keuze = input("Dus, ga je mee of niet? (ja/nee): ").lower()
            else:
                print("Ongeldige keuze. Probeer opnieuw.")
        elif keuze == "ja":
            # Speler wordt voorgesteld aan de Yakuza
            print("Je gaat met de man mee naar een geheime locatie.")
            print("Daar word je voorgesteld aan de Yakuza-drugsbazen.")
            print("Ze vragen je of je de Yakuza-clan wilt joinen.")
            yakuza_keuze = input("Wil je de Yakuza-clan joinen? (ja/nee): ").lower()

            if yakuza_keuze == "ja":
                print("Je krijgt 10 miljoen euro en gaat meteen op je eerste missie.")
                print("Je eerste missie is het assisineren van een rijke, belangrijke vrouw en haar baby.")
                missie_keuze = input("Kies je ervoor om de vrouw en baby te assisineren of jezelf te doden? (assisineren/zelfmoord): ").lower()

                if missie_keuze == "assisineren":
                    print("Je voert de missie succesvol uit en wint het spel!")
                    print_gewonnen()
                    return
                elif missie_keuze == "zelfmoord":
                    print("Je kiest ervoor om jezelf te doden omdat je dit niet wilt.")
                    print("Game Over.")
                    return
                else:
                    print("Ongeldige keuze. Probeer opnieuw.")
            elif yakuza_keuze == "nee":
                print("Je wordt gestoken met een injectienaald en valt in slaap.")
                print("Je wordt in een auto gestopt, maar je wordt wakker en voelt je verzwakt.")
                ontsnappen_keuze = input("Probeer je te ontsnappen? (ja/nee): ").lower()

                if ontsnappen_keuze == "nee":
                    print("Er wordt nog een injectienaald in je gespoten, wat leidt tot je dood.")
                    print("Game Over.")
                    return
                elif ontsnappen_keuze == "ja":
                    print("Je breekt het achterraam van de auto en ontsnapt.")
                    print("Je steelt een andere auto en moet kiezen: links of rechts.")
                    richting_keuze = input("Kies je richting (links/rechts): ").lower()

                    if richting_keuze == "links":
                        print("Je rijdt per ongeluk van een half afgemaakt viaduct af en gaat dood.")
                        print("Game Over.")
                        return
                    elif richting_keuze == "rechts":
                        print("Je weet de ontvoerders en Yakuza-clanleden af te schudden.")
                        print("Je wint het spel en bent vrij!")
                        print_gewonnen()
                        return
                    else:
                        print("Ongeldige keuze. Probeer opnieuw.")
                else:
                    print("Ongeldige keuze. Probeer opnieuw.")
            else:
                print("Ongeldige keuze. Probeer opnieuw.")
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
            keuze = input("Ga je mee? (ja/nee): ").lower()


def vliegveld_keuze():
    # Speler kiest een land om naar toe te vliegen
    print("Je komt aan bij het vliegveld en hebt de keuze uit drie landen om naar toe te gaan.")
    print("Kies een land: 'Mexico', 'Noord-Korea', of 'Japan'")
    land = input("> ").lower()

    if land == "mexico":
        mexico_verhaal()
    elif land == "noord-korea":
        print("Je vliegt naar Noord-Korea.")
        print("Helaas word je bij aankomst meteen gearresteerd en vermoord.")
        print("Game Over.")
    elif land == "japan":
        japan_verhaal()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        vliegveld_keuze()


def start_game():
    # Start de game
    print_welkom()
    print("Welkom bij jouw avontuur!")
    print("Je avontuur begint hier. Kies je eigen pad.")
    print("Typ 'John Pork' om met John Pork mee te gaan.")
    print("Typ 'Chill Guy' om Chill Guy te volgen.")

    keuze = input("> ").lower()

    if keuze == "john pork":
        john_pork_pad()
    elif keuze == "chill guy":
        chill_guy_pad()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        start_game()


start_game()