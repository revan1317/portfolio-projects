def print_ascii(fn):
    try:
        with open(fn, 'r') as bestand:
            print(bestand.read())
    except FileNotFoundError:
        print(f"Bestand {fn} niet gevonden.")   # wat daadwerklijk de ascii print


def kiesprint(keuze):
    # bepaalt welke ascii jij wilt dat de printer print
    if keuze == '1':
        print_ascii('plaatjes_slots/jackpot.txt')
    elif keuze == '2':
        print_ascii('plaatjes_slots/seven.txt')
    elif keuze == '3':
        print_ascii('plaatjes_slots/hart.txt')
    elif keuze == '4':
        print_ascii('plaatjes_slots/diamand.txt')
    elif keuze == '5':
        print_ascii('plaatjes_slots/fail.txt')
    elif keuze == '6':
        print_ascii('plaatjes_slots/slotstittle.txt')   # print het tittle scherm voor slots
    elif keuze == '7':
        print_ascii('plaatjes_slots/black_jack_start.txt')   # print het tittle scherm voor black Jack
