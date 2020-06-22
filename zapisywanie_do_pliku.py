file = open("nowy.txt", "w")
file.write("Nowy tekst")
file.close()

# nadpisywanie pliku

file = open("nowy.txt", "w")
file.write("Zupelnie nowy tekst")
file.close()

# dodawanie tekstu do pliku

file = open("nowy.txt", "a")
file.write(" Zupelnie nowy tekst")
file.close()