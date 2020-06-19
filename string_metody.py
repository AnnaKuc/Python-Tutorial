imie = 'Anna'
nazwisko = "Kuc 'Kowalska'"
adres = '''Ogrodnicza 22/2
    Bialystok 00-002'''

print(imie)
print(nazwisko)
print(adres)

print('Czytam ksiazke "Pasja testowania"')
print('Czytam \t ksiazke \n "Pasja testowania"')
print(r'Czytam \t ksiazke \n "Pasja testowania"')
print('\\Czytam \t ksiazke \n "Pasja testowania"')

print("male litery".upper())
print("DUZE LITERY".lower())

print(imie.islower())
print(nazwisko.isupper())

for char in 'Anna':
    print(char)

print(imie[0])
print(nazwisko[1:3])
print(imie.index("a"))

print("Ala" in "Ala ma kota")
print("Ala" not in "Ala ma kota")

print(" ".join(["Ala", "ma", "kota"]))
print("Ala,ma,kota,i,psa".split(","))

print(imie.startswith("An"))
print(imie.endswith("na"))