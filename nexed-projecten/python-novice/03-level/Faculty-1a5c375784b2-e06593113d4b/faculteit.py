n = int(input("Van welk getal wil je de faculteit weten?"))
faculteit = 1

for i in range(1, n + 1):
    faculteit *= i

print(f"De faculteit van {n} is {faculteit}")
