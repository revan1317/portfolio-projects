class CurrencySystem:
    # Zorgt ervoor dat als je een ander currency kiest dat je het juiste aantal geld krijgt
    eenheden = {
        "EUR": 1.0,
        "USD": 1.09,
        "GBP": 0.84
    }

    def __init__(self, saldo, currency="EUR"):
        self.saldo = saldo
        self.currency = currency

    def convert_to_currency(self, amount, target_currency):
        if target_currency not in self.eenheden:
            raise ValueError("Ongeldige valuta.")
        return amount * (self.eenheden[target_currency] / self.eenheden[self.currency])


def kies_valuta():
    while True:
        currency = input("Kies je valuta (EUR, USD, GBP): ").upper()
        if currency in CurrencySystem.eenheden:
            return currency
        print("Ongeldige valuta. Kies uit EUR, USD of GBP.")


valuta = kies_valuta()
currency_system = CurrencySystem(valuta)
