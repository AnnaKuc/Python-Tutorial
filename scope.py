imie = "Anna"
nazwisko = "Kuc"

def przedstaw_sie():
    global nazwisko
    nazwisko = "Kowalska"
    print(imie)
    print(nazwisko)

print(imie)
print(nazwisko)
przedstaw_sie()
print(nazwisko)