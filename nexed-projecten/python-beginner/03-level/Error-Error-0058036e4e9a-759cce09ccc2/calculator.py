geldige_operaties = ["+", "-", "*", "/", "%"]

operatie = input("Operatie? (+, -, *, /, %): ")

if operatie not in geldige_operaties:
    print(f"{operatie} is geen geldige operatie. Kies een van +, -, *, / of %")
    exit()

eerste_input = input("Eerste getal? ")

if eerste_input.find(',') != -1:
    print(f"Kan '{eerste_input}' niet omzetten naar een getal. Zorg dat je '.' gebruikt in plaats van ','.")
    exit()

try:
    eerstegetal = float(eerste_input)
except ValueError as e:
    print(f"Kan {eerste_input} niet omzetten naar een getal. Zorg dat je '.' gebruikt in plaats van ','.")
    exit()

tweede_input = input("Tweede getal? ")
try:
    tweedegetal = float(tweede_input)
except ValueError as e:
    print(f"Kan {tweede_input} niet omzetten naar een getal. Zorg dat je '.' gebruikt in plaats van ','.")
    exit()

if operatie == "+":
    resultaat = eerstegetal + tweedegetal
elif operatie == "-":
    resultaat = eerstegetal - tweedegetal
elif operatie == "*":
    resultaat = eerstegetal * tweedegetal
elif operatie == "/":
    resultaat = "Kan niet delen door 0" if tweedegetal == 0 else eerstegetal / tweedegetal
elif operatie == "%":
    resultaat = "Kan niet delen door 0" if tweedegetal == 0 else eerstegetal % tweedegetal

print("Resultaat:", resultaat)
