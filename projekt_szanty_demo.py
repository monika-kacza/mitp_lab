import time

print("Witaj w grze 'Szanta na sukces'!\nZapoznaj się z treścią szanty, a następnie odgadnij jej tutuł.")
time.sleep(5)

text_szanty = "Okręt nasz wpłynął w mgłę i fregaty dwie\nPopłynęły naszym kursem by nie zgubić się.\nPotem szkwał wypchnął nas poza mleczny pas\nI nikt wtedy nie przypuszczał, że fregaty śmierć nam niosą.\nCiepła krew poleje się strugami,\nWygra ten, kto utrzyma ship.\nW huku dział ktoś przykryje się falami,\nJak da Bóg, ocalimy bryg."


delay_per_line = 0.5

delay_per_char = 0.05

for line in text_szanty.splitlines():
    if line.strip() == "":
        continue

    print(line)
    time.sleep(delay_per_line)

    for char in line:

        time.sleep(delay_per_char)

print(text_szanty)
print()

szanta = input("Jaka to szanta?  ")
szanta_odp = "Bitwa"

if szanta.lower() == szanta_odp.lower():
    print("Poprawna odpowiedź!")

else:
    print("Prawie! Ta szanta nosi tytuł 'Bitwa'")
