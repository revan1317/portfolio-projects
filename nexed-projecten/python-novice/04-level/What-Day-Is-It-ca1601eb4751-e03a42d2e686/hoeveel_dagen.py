from datetime import datetime

jaar = int(input("Wat is het jaar? "))
maand = int(input("Wat is het maandnummer? "))
dag = int(input("Wat is de dag? "))

datum = datetime(jaar, maand, dag)
vandaag = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
verschil = vandaag - datum

print(f"{verschil.days} days")
