while True:
    try:
        print("Podaj pierwsza liczbe:")
        pierwsza_liczba = int(input())
        print("Podaj druga liczbe:")
        druga_liczba = int(input())
        print(pierwsza_liczba + druga_liczba)
        break
    except ValueError:
        print("Podales bledna wartosc")
        print("Sprobuj jeszcze raz")
        continue