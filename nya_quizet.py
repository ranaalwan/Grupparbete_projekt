score = 0
fel_svar = 0

def answer_check(players_answer, right_answer, right_answer2):
    global score
    global fel_svar
    tries = 2
    if players_answer == right_answer or players_answer == right_answer2:
        score += 1
        print(f"Du har rätt! Dina poäng: {score}\n")

    else:
        while True:
            print(f"Du har fel! Testa igen. Försök kvar: {tries}\n")
            tries -= 1
            players_answer = input("Svar: ").lower()
            if players_answer == right_answer or players_answer == right_answer2:
                score += 1
                print(f"Du har rätt!\nDina poäng: {score}")
                break
            elif tries == 0:
                print(f"Inga mer försök!")
                fel_svar += 1
                break

print("\n**********************VÄLKOMMEN TILL PYTHON-QUIZET!**********************")            

print("""\nFråga 1: Vad är Python?\n
1. Ett programmeringsspråk
2. Ett spel
3. En knapp\nSvar: """, end='')
answer_check(input().lower(), "1", "ett programmeringsspråk")

print("\n----------------------------------------------------------------------\n")

print("""Fråga 2: Vad är ett exempel på en datatyp?\n
1. En dator
2. En string
3. Ett äpple\nSvar: """, end='')
answer_check(input().lower(),"2", "en string")

print("----------------------------------------------------------------------\n")

print("""Fråga 3: När skapades Python?\n
1. 1991
2. 1989
3. 1977\nSvar: """, end='')
answer_check(input().lower(), "1", "1991")

print("----------------------------------------------------------------------\n")

print("""Fråga 4: Hur skriver man en lista?\n
1. ()
2. {}
3. []\nSvar: """, end='')
answer_check(input().lower(), "3", "[]")

print("----------------------------------------------------------------------\n")

print("""Fråga 5: Dictionary har två delar, vad är de?\n
1. value - function
2. int - loop
3. key - value\nSvar: """, end='')
answer_check(input().lower(), "3", "key - value")

print("----------------------------------------------------------------------\n")

print("""Fråga 6: Vad för typ av språk är Python?\n
1. High-level språk
2. Hemligt språk
3. Low-level språk\nSvar: """, end='')
answer_check(input().lower(), "1", "high-level språk")

print("----------------------------------------------------------------------\n")

print("""Fråga 7: Vad är korrekta syntaxen för att få output 'Hello World!' i Python?\n
1. echo("Hello World!")
2. print("Hello World!")
3. console("Hello World!")\nSvar: """, end='')
answer_check(input().lower(), "2", "print("Hello World!")")

print("----------------------------------------------------------------------\n")

print("""Fråga 8: Vad kan man göra i Python?\n
1. Kolla på film
2. Programmera applikationer
3. Live-sändningar\nSvar: """, end='')
answer_check(input().lower(), "2", "programmera applikationer")

print("----------------------------------------------------------------------\n")

print("""Fråga 9: Vad finns det för olika typer av loopar?\n
1. for och while
2. floor och well
3. four och with\nSvar: """, end='')
answer_check(input().lower(), "1", "for och while")

print("----------------------------------------------------------------------\n")

print("""Fråga 10: Hur skriver man en funktion?\n
1. deph = {'funktionnamn'}
2. däf innit('funktionnamn'):
3. def 'funktionnamn'():\nSvar: """, end='')
answer_check(input().lower(), "3", "def 'funktionnamn'():")

if fel_svar == 0:
    print("\nGRATTIS! Du fick alla rätt.")
print("----------------------------------------------------------------------\n")
