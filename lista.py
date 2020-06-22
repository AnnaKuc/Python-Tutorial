imiona = ["Basia", "Kasia", "Asia", 2, 4, 6, 8, 10]
print(imiona)
print(imiona[0])
print(imiona[6])
print(imiona[-1])
print(imiona[0:3])
print(imiona.index("Asia"))

imiona.append("Iwona")
imiona.insert(1, "Genowefa")
print(imiona)
print(len(imiona))

imiona.remove("Asia")
print(imiona)
del imiona[1]
print(imiona)

pierwsza_lista = ["kubek", "lampa", "biurko"]
druga_lista = ["tablica", "telefon", "ksiazka", 1, 2, 3]
print(pierwsza_lista*3)
print(pierwsza_lista + druga_lista)

pierwsza_lista.sort()
print(pierwsza_lista)

biurko, kubek, lampa = pierwsza_lista
print(biurko)
print(kubek)
print(lampa)

ksiazki = ["pierwsza ksiazka", "druga ksiazka", "trzecia ksiazka"]
alfabetycznie = sorted(ksiazki)
od_konca = sorted(ksiazki, reverse=True)
print(ksiazki)
print(alfabetycznie)
print(od_konca)

