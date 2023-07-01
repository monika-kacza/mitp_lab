print("Przyszła pora na pytania otwarte!")
print("Przed Tobą 10 pytań, na które musisz odpowiedzieć dokładnie jednym słowem.\nPowodzenia!")
print()
def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        user_answer = input(question + " ")
        if user_answer.lower() == answer.lower():
            print("Odpowiedź poprawna!")
            score += 1
        else:
            print("Odpowiedź niepoprawna!")
            print("Poprawna odpowiedź to:", answer)
        print()
    print("Twój wynik to:", score, "na", len(questions))

quiz_questions = {
    "Pytanie 1: Skala Petersena służy do określania stanu:": "Morza",
    "Pytanie 2: Jak nazywa się urządzenie, którym mierzymy prędkość wiatru": "Anemometr",
    "Pytanie 3: Chmura Cirrostratus zwiastuje nadejście:": "Opadów",
    "Pytanie 4: Jak nazywamy dział nauki opisujący wody żeglowne i ich oznakowanie?": "Locja",
    "Pytanie 5: Jak nazywa się element służący do ochrony pędnika?": "Ostroga",
    "Pytanie 6: Łódź ślizgowa, nadmuchiwana, ze sztywnym dnem, to łódź typu:": "RIB",
    "Pytanie 7: W jaki sposób cumujemy jacht w śluzie komorowej?": "Nabiegowo",
    "Pytanie 8: Jak nazywa się warstwa atmosfery, w której zachodzi większość procesów kształtujących pogodę?": "Troposfera",
    "Pytanie 9: Jak nazywa się schowek na dziobie jachtu?": "Forpik",
    "Pytanie 10: Kurs, w którym wiatr wieje z kierunku pomiędzy rufą, a trawersem jachtu to:": "Baksztag"

}

run_quiz(quiz_questions)
