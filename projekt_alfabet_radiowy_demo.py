alfabet_fonetyczny = {
    "A": "Alfa",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu"
}

def zapisz_wiadomosc_fonetycznie(wiadomosc):
    wiadomosc_fonetyczna = []
    for litera in wiadomosc.upper():
        if litera.isalpha():
            if litera in alfabet_fonetyczny:
                wiadomosc_fonetyczna.append(alfabet_fonetyczny[litera])
            else:
                wiadomosc_fonetyczna.append(litera)
    return " ".join(wiadomosc_fonetyczna)

print("Alfabet radiowy, znany również jako Alfabet fonetyczny NATO czy Międzynarodowy alfabet fonetyczny to najbardziej\nrozpowszechniony system literowania wyrazów w pewnych specyficznych zastosowaniach, np. w żeglarstwie podczas\nprowadzenia komunikacji radiowej, gdzie każdej literze alfabetu odpowiada ustalone słowo.")
print("Przetestuj jak działa - postepuj zgodnie z poleceniami.")
print("Na końcu przekonasz się, jak taki alfabet wygląda!")
print()

for _ in range(3):
    wiadomosc_uzytkownika = input("Wpisz wiadomość: ")
    wiadomosc_fonetyczna = zapisz_wiadomosc_fonetycznie(wiadomosc_uzytkownika)
    print("Wiadomość fonetyczna:", wiadomosc_fonetyczna)

print(alfabet_fonetyczny)
