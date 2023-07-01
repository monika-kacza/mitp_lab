class Jacht:
    def __init__(self, nazwa, model, rocznik):
        self.nazwa = nazwa
        self.model = model
        self.rocznik = rocznik

    def plywaj(self, jezioro, port=None):
        if port:
            print(f"Popłyniesz jachtem {jacht1.nazwa} na jezioro {jezioro} do portu {port}.")
        else:
            print(f"Popłyniesz na jezioro {jezioro}.")

print("Witaj w Twojej żeglarskiej przygodzie!")
print("Na początek wybierz, jakim jachtem chcesz płynąć.")
nazwa = input("Podaj nazwę jachtu: ")
model = input("Podaj model jachtu: ")
rocznik = input("Podaj rocznik jachtu: ")


jacht1 = Jacht(nazwa, model, rocznik)



print("Zaplanuj z nami dokąd popłyniesz. Wyruszamy z portu Piękny Brzeg!")
print(f"Masz do dyspozycji jacht {jacht1.model} o nazwie {jacht1.nazwa}, rocznik {jacht1.rocznik}.")

while True:
    print("\nCo chcesz zrobić?")
    print("1. Zaplanuj trasę")
    print("2. Zakończ planowanie")

    wybor = input("Twój wybór: ")

    if wybor == "1":
        print("Wybierz jezioro:")
        print("1. Mamry")
        print("2. Dargin")
        print("3. Niegocin")
        jezioro = input("Twój wybór: ")

        if jezioro == "1":
            print("Wybierz port:")
            print("1. Kietlice")
            print("2. Kętrzyńska Przystań")
            print("3. Skłodowo")
            print("4. Mamerki")
            print("5. Powrót do Pięknego Brzegu")
            port = input("Twój wybór: ")
            if port == "1":
                jacht1.plywaj("Mamry", "Kietlice")
            elif port == "2":
                jacht1.plywaj("Mamry", "Kętrzyńska Przystań")
            elif port == "3":
                jacht1.plywaj("Mamry", "Skłodowo")
            elif port == "4":
                jacht1.plywaj("Mamry", "Mamerki")
            elif port == "5":
                jacht1.plywaj("Święcajty", "Piękny Brzeg")
            else:
                print("Niepoprawny wybór portu.")
        elif jezioro == "2":
            print("Wybierz port:")
            print("1. Roganty")
            print("2. Nowy Harsz")
            print("3. Zdorkowo")
            print("4. Powrót do Pięknego Brzegu")
            port = input("Twój wybór: ")
            if port == "1":
                jacht1.plywaj("Dargin", "Roganty")
            elif port == "2":
                jacht1.plywaj("Dargin", "Nowy Harsz")
            elif port == "3":
                jacht1.plywaj("Dargin", "Zdorkowo")
            elif port == "4":
                jacht1.plywaj("Święcajty", "Piękny Brzeg")
            else:
                print("Niepoprawny wybór portu.")
        elif jezioro == "3":
            print("Wybierz port:")
            print("1. Ekomarina Giżycko")
            print("2. AZS Wilkasy")
            print("3. Resort Niegocin")
            print("4. Powrót do Pięknego Brzegu")
            port = input("Twój wybór: ")
            if port == "1":
                jacht1.plywaj("Niegocin", "Ekomarina Giżycko")
            elif port == "2":
                jacht1.plywaj("Niegocin", "AZS Wilkasy")
            elif port == "3":
                jacht1.plywaj("Niegocin", "Resort Niegocin")
            elif port == "4":
                jacht1.plywaj("Święcajty", "Piękny Brzeg")
            else:
                print("Niepoprawny wybór portu.")
        else:
            print("Niepoprawny wybór jeziora.")

    elif wybor == "2":
        print("Zakończono planowanie.")
        break
    else:
        print("Niepoprawny wybór. Spróbuj ponownie.")
