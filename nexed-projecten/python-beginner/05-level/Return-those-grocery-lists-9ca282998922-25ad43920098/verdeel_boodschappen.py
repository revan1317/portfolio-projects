boodschappenlijst = ['bloem', 'ei', 'boter', 'ei', 'melk', 'vanille', 'suiker', 'boter', 'walnoten', 'boter', 'melk', 'ei', 'kaarsjes', 'fondant']

def verdeel_boodschappen(lijst):
    lijst_1 = lijst[::2]
    lijst_2 = lijst[1::2]
    return lijst_1, lijst_2

tim_lijst, youssef_lijst = verdeel_boodschappen(boodschappenlijst)

print(f"Tim's lijst is: {tim_lijst}")
print(f"Youssef's lijst is: {youssef_lijst}")
