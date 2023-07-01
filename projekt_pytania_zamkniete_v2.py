def load_questions(file_name):
    questions = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
        num_questions = len(lines) //7

        for i in range(num_questions):
            question_start = (i+1) * 7
            question = lines[question_start].strip()
            answers = lines[question_start + 1:question_start + 5]
            correct_answer = lines[question_start + 5].strip()
            questions.append([question, answers, correct_answer])
    return questions


def run_quiz(questions):
    score = 0
    for i, question in enumerate(questions):
        print(f"Pytanie {i+1}: {question[0]}")
        for j, answer in enumerate(question[1]):
            print(f"{answer.strip()}")
        user_answer = input("Twoja odpowiedź (A, B, C, lub D): ").upper()
        if user_answer == question[2]:
            print("Poprawna odpowiedź!")
            score += 1
        else:
            print("Niepoprawna odpowiedź!")
        print()

    total_questions = len(questions)
    print(f"Koniec tej części quizu! Twój wynik:  {score}/{total_questions}.")

print("Pora na pytania zamknięte! Odpowiedz poprawnie na 20 pytań, do wyboru masz trzy odpowiedzi A, B lub C. Tylko jedna z nich jest poprawna. Powodzenia!")
print()
file_name = "pytania_zamkniete.txt"
questions = load_questions(file_name)
run_quiz(questions)
