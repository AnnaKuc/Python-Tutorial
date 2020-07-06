class Pies:

    gatunek = "pies domowy"

    def __init__(self, rasa, imie, wiek):
        print("Wewnatrz metody init")
        self.rasa = rasa
        self.imie = imie
        self.wiek = wiek

    def szczekaj(self):
        return "Hau, hau!"

    def zaprezentuj_psa(self):
        print("Imie to " + self.imie)
        print("Rasa to " + self.rasa)
        print("Wiek psa to " + str(self.wiek) + " lata")


Reksio = Pies("kundel", "Reksio", 2)

print(Reksio.imie)
print(Reksio.rasa)

print(Reksio.gatunek)
print(Pies.gatunek)

print(Reksio.wiek)
Reksio.wiek = 3
print(Reksio.wiek)

Reksio.gatunek = "ptak"
print(Reksio.gatunek)

print(Reksio.szczekaj())
Reksio.zaprezentuj_psa()