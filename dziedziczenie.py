class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "Nazywam sie " + self.imie + " " + self.nazwisko

class Student(Osoba):

    def __init__(self, imie, nazwisko, numer_indeksu):
        Osoba.__init__(self, imie, nazwisko)
        self.indeks = numer_indeksu

    def podaj_nr_indeksu(self):
        return self.indeks

    def przedstaw_sie(self):
        return "Jestem studentem i mam na imie " + self.imie

student = Student("Ania", "Kuc", 123456)
print(student.przedstaw_sie())
print(student.podaj_nr_indeksu())

osoba = Osoba("Ania", "Kuc")
print(osoba.przedstaw_sie())