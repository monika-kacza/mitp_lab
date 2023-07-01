import os
import importlib.util

def run_game(file_name):
    os.system('cls' if os.name == 'nt' else 'clear')
    spec = importlib.util.spec_from_file_location("game_module", file_name)
    game_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(game_module)

imie = input("Jak masz na imię? ")
print(f"Cześć {imie}!")
print()
print ("Witaj w Wielkim Quizie Żeglarskim!")
print ("Pomoże Ci się on przygotować do egzaminu teoretycznego na stopień żeglarza jachtowego.")
print ("Przed Tobą kilka modułów, które umilą Ci przygotowania.")
print ("Część zadań zawiera pytania, które napotkasz na egzaminie. Pozostałe elementy to mini gry, które rozluźnią Cię przed dalszymi testami. Miłej zabawy!")


while True:
    print("--------------------")
    print("Dostępne gry:")
    print("1. Poznaj alfabet radiowy")
    print("2. Zaplanuj trasę po Mazurach")
    print("3. Pytania teoretycznie otwarte")
    print("4. Pytania teoretycznie zamknięte")
    print("5. Co wiesz o ratownictwie?")
    print("6. Regaty jachtowe")
    print("7. Szanta na sukces")

    while True:
        wybor = input("Wybierz numer gry (1-7) lub wpisz 'q' aby wyjść: ")

        if wybor == '1':
            file_name = "/Users/monia/PycharmProjects/pythonProject/MITP/projekt_alfabet_radiowy_demo.py"
            run_game(file_name)
            break
        elif wybor == '2':
            file_name = "/Users/monia/PycharmProjects/pythonProject/MITP/projekt_planowanie_trasy.py"
            run_game(file_name)
            break
        elif wybor == '3':
            file_name = "/Users/monia/PycharmProjects/pythonProject/MITP/projekt_pytania_otwarte.py"
            run_game(file_name)
            break
        elif wybor == '4':
            file_name = "/Users/monia/PycharmProjects/pythonProject/MITP/projekt_pytania_zamkniete_v2.py"
            run_game(file_name)
            break
        elif wybor == '5':
            file_name = "/Users/monia/PycharmProjects/pythonProject/MITP/projekt_ratownictwo.py"
            run_game(file_name)
            break
        elif wybor == '6':
            file_name = "/Users/monia/PycharmProjects/pythonProject/MITP/projekt_regaty.py"
            run_game(file_name)
            break
        elif wybor == '7':
            file_name = "/Users/monia/PycharmProjects/pythonProject/MITP/projekt_szanty_demo.py"
            run_game(file_name)
            break
        elif wybor.lower() == 'q':
            print("Dzięki za udział w grze! Mamy nadzieję, że jeszcze nas odwiedzisz. Stopy wody pod kilem i powodzenia na egzaminie!")
            exit()
        else:
            print("Niepoprawny wybór. Spróbuj jeszcze raz.")
            continue

    print()

