def rzeczy(pierwsza_rzecz, *args):
    print(pierwsza_rzecz)
    print(args[0])
    for arg in args:
        print(arg)

rzeczy("stol", "lozko", "lampa", "koc")

def dziennik(klasa="1 c", **kwargs):
    print("Klasa " + klasa)
    for nazwisko in kwargs.keys():
        print(nazwisko)
    print(kwargs.get("Kowalski"))

dziennik("3 c", Kowalski=1, Nowak=2, Wisniewski=3)