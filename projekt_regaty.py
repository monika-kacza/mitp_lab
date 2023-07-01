import random

class Jacht:
    def __init__(self, nazwa, szybkosc):
        self.nazwa = nazwa
        self.szybkosc = szybkosc

    def przyspiesz(self):
        self.szybkosc += random.randint(1, 5)

    def zwolnij(self):
        if self.szybkosc > 0:
            self.szybkosc -= random.randint(1, 3)

    def pokaz_predkosc(self):
        print(f"{self.nazwa}: {self.szybkosc} węzłów")

    def __str__(self):
        return self.nazwa


jacht1 = Jacht("Maxus 33.1 RS ", 10)
jacht2 = Jacht("Phila 880", 12)
jacht3 = Jacht("Twister 800n", 8)


print("Witaj w symulacji regat!")
print()
print(f"Jachty biorące udział w regatach to {jacht1}, {jacht2} i {jacht3}.")
print()
print("Dostępne polecenia: przyspiesz, zwolnij, predkosci, koniec")

while True:
    polecenie = input("Wprowadź polecenie: ")

    if polecenie.lower() == "przyspiesz":
        jacht1.przyspiesz()
        jacht2.przyspiesz()
        jacht3.przyspiesz()
        print("Jachty przyspieszyły!")

    elif polecenie.lower() == "zwolnij":
        jacht1.zwolnij()
        jacht2.zwolnij()
        jacht3.zwolnij()
        print("Jachty zwolniły!")

    elif polecenie.lower() == "predkosci":
        print("Aktualne prędkości jachtów:")
        jacht1.pokaz_predkosc()
        jacht2.pokaz_predkosc()
        jacht3.pokaz_predkosc()

    elif polecenie.lower() == "koniec":
        print("Dziękujemy za grę!")
        break

    else:
        print("Niepoprawne polecenie. Spróbuj jeszcze raz.")

    print()
    print("Aktualne prędkości jachtów:")
    jacht1.pokaz_predkosc()
    jacht2.pokaz_predkosc()
    jacht3.pokaz_predkosc()


najwyzsza_predkosc = max(jacht1.szybkosc, jacht2.szybkosc, jacht3.szybkosc)
if najwyzsza_predkosc == jacht1.szybkosc:
    print(f"Jacht {jacht1} wygrał regaty!")
elif najwyzsza_predkosc == jacht2.szybkosc:
    print(f"Jacht {jacht2} wygrał regaty!")
else:
    print(f"Jacht {jacht3} wygrał regaty!")
