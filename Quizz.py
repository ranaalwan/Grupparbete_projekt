

score = 0

def answer_check(right_answer, right_answer2):
    global players_answer
    global score

    if players_answer == right_answer or players_answer == right_answer2:
        score += 1
        print(f"Du har rätt! Dina poäng: {score}\n")

    else:
        print(f"Du har fel!")

print("\n**********************VÄLKOMMEN TILL QUIZET!**********************")            

print("""\nFråga 1: Vad är Python?\n
1. Ett programmeringsspråk
2. Ett spel
3. En knapp\n""")
players_answer = input("Svar: ").lower()
answer_check("1", "ett programmeringsspråk")

print("----------------------------------------------------------------------\n")

print("""Fråga 2: Vad är ett exempel på en datatyp?\n
1. En dator
2. En string
3. Ett äpple\n""")
players_answer = input("Svar: ").lower()
answer_check("2", "en string")

print("----------------------------------------------------------------------\n")

print("""Fråga 3: När skapades Python?\n
1. 1991
2. 1989
3. 1977\n""")
players_answer = input("Svar: ").lower()
answer_check("1", "1991")

print("----------------------------------------------------------------------\n")

print("""Fråga 4: Hur skriver man en lista?\n
1. ()
2. {}
3. []\n""")
players_answer = input("Svar: ").lower()
answer_check("3", "[]")

print("----------------------------------------------------------------------\n")

print("""Fråga 5: Dictionary har två delar, vad är de?\n
1. value - function
2. int - loop
3. key - value\n""")
players_answer = input("Svar: ").lower()
answer_check("3", "key - value")

print("----------------------------------------------------------------------\n")

print("""Fråga 6: Vad för typ av språk är Python?\n
1. High-level språk
2. Hemligt språk
3. Low-level språk\n""")
players_answer = input("Svar: ").lower()
answer_check("1", "high-level språk")

print("----------------------------------------------------------------------\n")

print("""Fråga 7: Vad är korrekta syntaxen för att få output "Hello World!" i Python?\n
1. echo("Hello World!")
2. print("Hello World!")
3. console("Hello World!")\n""")
players_answer = input("Svar: ").lower()
answer_check("2", "en string")

print("----------------------------------------------------------------------\n")

print("""Fråga 8: Vad kan man göra i Python?\n
1. Kolla på film
2. Programmera applikationer
3. Live-sändningar\n""")
players_answer = input("Svar: ").lower()
answer_check("2", "programmera applikationer")

print("----------------------------------------------------------------------\n")

print("""Fråga 9: Vad finns det för olika typer av loopar?\n
1. for och while
2. floor och well
3. four och with\n""")
players_answer = input("Svar: ").lower()
answer_check("1", "for och while")

print("----------------------------------------------------------------------\n")

print("""Fråga 10: Hur skriver man en funktion?\n
1. deph = {'funktionnamn'}
2. däf innit('funktionnamn'):
3. def 'funktionnamn'():\n""")
players_answer = input("Svar: ").lower()
answer_check("3", "def 'funktionnamn'():")

print("----------------------------------------------------------------------\n")













