pierwszy_zbior = {"Bialystok", "Warszawa", "Wroclaw"}
drugi_zbior = {"Bialystok"}

print(pierwszy_zbior)
pierwszy_zbior.add("Lodz")
print(pierwszy_zbior)
pierwszy_zbior.add("Warszawa")
print(pierwszy_zbior)

print("Operacje na zbiorach")
print(pierwszy_zbior - drugi_zbior)
print(pierwszy_zbior | drugi_zbior)
print(pierwszy_zbior & drugi_zbior)
print(pierwszy_zbior ^ drugi_zbior)

print(type(pierwszy_zbior))

# zbory nie wspieraja indeksowania
# print(pierwszy_zbior[0])