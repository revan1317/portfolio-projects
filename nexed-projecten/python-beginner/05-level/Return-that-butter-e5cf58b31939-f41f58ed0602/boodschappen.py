def tel_product(lijst, product):
    return lijst.count(product)

boodschappenlijst = ["melk", "boter", "kaas", "boter", "brood", "boter"]

aantal_boter = tel_product(boodschappenlijst, "boter")

totaal_boter = aantal_boter + 3

print(f"In totaal heb ik {totaal_boter} pakjes boter nodig.")
