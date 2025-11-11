import random
from plaatjes_slots import printer as printer
import basis


# bekijkt welk figuur je hebt gerolled
def rollbekijker(rollint):
    if rollint < 10:
        return '1'  # jackpot
    elif rollint < 25:
        return '2'  # seven
    elif rollint < 50:
        return '3'  # hart
    elif rollint < 75:
        return '4'  # diamant
    return '5'  # fail


# geeft de rewards als dit van toepassing is
def beloninggever(teken):
    if teken == '4':
        print("3 diamanten +50!!!")
        basis.balans += 50
    elif teken == '3':
        print("3 harten +75!!!")
        basis.balans += 75
    elif teken == '2':
        print("3 sevens +150!!!")
        basis.balans += 150
    elif teken == '1':
        print("3 jackpots +300!!!")
        basis.balans += 300


# de slots rol die je doet als je start
def rol():

    basis.balans -= 10

    resultaat_een = random.randint(0, 100)
    printer.kiesprint(rollbekijker(resultaat_een))

    resultaat_twee = random.randint(0, 100)
    printer.kiesprint(rollbekijker(resultaat_twee))

    resultaat_drie = random.randint(0, 100)
    printer.kiesprint(rollbekijker(resultaat_drie))

    if rollbekijker(resultaat_een) == rollbekijker(resultaat_twee) == rollbekijker(resultaat_drie):
        beloninggever(rollbekijker(resultaat_een))
    else:
        for resultaat in [resultaat_een, resultaat_twee, resultaat_drie]:
            if rollbekijker(resultaat) == '1':
                print("Jackpot +20!!")
                basis.balans += 20
    start()


# start het spel
def start():
    print(basis.balans)
    printer.kiesprint('6')
    keuze = input("Druk op enter om te beginnen of type 'exit' om te stoppen\nRoll NU!:")

    # sluit spel
    if keuze == 'exit':
        basis.start()

    # start spel
    basis.schoonmaker()
    rol()


start()
