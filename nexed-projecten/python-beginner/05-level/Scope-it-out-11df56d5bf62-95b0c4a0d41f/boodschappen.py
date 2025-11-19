boodschappenlijst = ["bloem", "ei", "boter", "melk", "vanille", "suiker"]

def overschrijf_boodschappen(lijst):
    lijst = ["wafels", "vruchtenhagel", "kwark"]
    print(f"Nieuwe lijst in functie: {lijst}")

overschrijf_boodschappen(boodschappenlijst)
print(f"Lijst na functieaanroep: {boodschappenlijst}")

def modify_boodschappen(lijst):
    lijst.append("kaarsjes")
    lijst.append("fondant")
    lijst.remove("boter")
    print(f"Geüpdatete lijst in functie: {lijst}")

modify_boodschappen(boodschappenlijst)
print(f"Lijst na functieaanroep: {boodschappenlijst}")
