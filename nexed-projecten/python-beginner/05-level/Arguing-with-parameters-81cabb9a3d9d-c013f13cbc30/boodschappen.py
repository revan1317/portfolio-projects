def tel_product(lijst, product):
    aantal = lijst.count(product)
    print(f"{product} komt {aantal} keer voor in de boodschappenlijst.")

boodschappenlijst = ["bloem", "ei", "boter", "ei", "melk", "vanille", "suiker", "boter", "cacao", "walnoten", "boter", "melk", "ei"]

tel_product(boodschappenlijst, "boter")
tel_product(boodschappenlijst, "ei")
tel_product(boodschappenlijst, "melk")
