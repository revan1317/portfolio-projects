operatie = input("Operatie? (+, -, *, /, %): ")
eerstegetal = float(input("Eerste getal? "))
tweedegetal = float(input("Tweede getal? "))

if operatie == "+":
    resultaat = eerstegetal + tweedegetal
elif operatie == "-":
    resultaat = eerstegetal - tweedegetal
elif operatie == "*":
    resultaat = eerstegetal * tweedegetal
elif operatie == "/":
    if tweedegetal == 0:
        resultaat = "Kan niet delen door 0"
    else:
        resultaat = eerstegetal / tweedegetal
elif operatie == "%":
    if tweedegetal == 0:
        resultaat = "Kan niet delen door 0"
    else:
        resultaat = eerstegetal % tweedegetal
else:
    resultaat = f"{operatie} is geen geldige operatie"

print("Resultaat:", resultaat)
