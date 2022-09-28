from turtle import pensize

score = 0    #För att räkna ihop poängen



question1 = input("När skapades Python?  \n(A) 1989 \n(B) 1991 \n(C) 2000 \n(D) 2008 \nSvar: ")
if question1 == "b" or question1 == "1991":     #Om användaren svarar rätt med någon av dessa alternativ kommer detta upp i terminalen
    score += 1
    print("Rätt svar")
    print("Poäng: ", score)
    print("\n")
else:    #Om användaren svarar fel kommer detta upp i treminalen
    print("Fel svar, rätta svaret är 1995.")
    print("Poäng: ", score)
    print("\n")


question2 = input("Vilket programerings språk tillhör Python? \n(A) Engelsk programering \n(B) Object Orienterad programering \n(C) WorlWide programing  \n(D) Compilerad programering \nSvar: ")
if question2 == "b" or question2 == "Object Orienterad programering":     #Användaren svarar rätt
    score += 1
    print("Rätt svar")
    print("Poäng: ", score)
    print("\n")
else:    #Användaren svarar fel
    print("Fel svar, rätta svaret är 1995.")
    print("Poäng: ", score)
    print("\n")



print("Du fick totalt", score, "/2 rätt!")    #Quiz är klart och totala poängen syns här
