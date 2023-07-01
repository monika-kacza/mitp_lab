
import random

pytania = (
    ("Jaki jest numer ratunkowy MOPR (Mazurskie Ochotnicze Pogotowie Ratunkowe?", "984"),
    ("Do jakiego kursu przechodzimy w przypadku pożaru na rufie?", "ostrego"),
    ("Dwie pozycje wydłużające czas przeżycia w wodzie to HELP i:  ", "clinch"),
    ("Stan, w którym temperatura ciała człowieka schodzi poniżej 35 stopni Celsjusza to: ", "hipotermia"),
    ("Jak inaczej nazywamy linę bezpieczeństwa?", "lajflina"),
)

def losuj_pytanie():
    return random.choice(pytania)

def rozpocznij_gre():
    print("Bezpieczeństwo i ratownictwo to nieodłączny element żeglugi.")
    print("Sprawdźmy Twoją wiedzę w tej dziedzinie!")
    print("Odpowiedz na pytania, aby zdobywać punkty.")

    punkty = 0
    while True:
        pytanie, odpowiedz = losuj_pytanie()
        print("\nPytanie:", pytanie)

        odpowiedz_gracza = input("Twoja odpowiedź: ").lower()

        if odpowiedz_gracza == odpowiedz:
            punkty += 1
            print("Odpowiedź poprawna!")
        else:
            print("Odpowiedź niepoprawna.")

        print("Aktualna liczba punktów:", punkty)

        wybor = input("Czy chcesz kontynuować? (tak/nie): ")
        if wybor.lower() != "tak":
            break

    print("Koniec! Zdobyte punkty:", punkty)

rozpocznij_gre()
