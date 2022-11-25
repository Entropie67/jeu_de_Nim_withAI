from random import choice

# Initiation de l'IA
AI = [[1, 2, 3] for i in range(10)]
AI.append([1, 2])
AI.append([1])

# Placement des allumettes
alu = [True for i in range(12)]
position = 0

# Variable d'abandon de l'IA
ab = False


def affichage():
    for a in alu:
        if a:
            print(" | ", end="")
        else:
            print("_")


game = True
p = ["Humain", "STURM 9000"]
i = 0
while game:
    affichage()
    print(f"\nAu tour de  : {p[i%2]}\n")
    if not i%2:
        juste = True
        while juste:
            choix = int(input(f"\n Votre choix (1, 2 ou 3) : "))
            if choix in [1, 2, 3]:
                juste = False
    else:
        print("IA")
        if len(AI[position]) == 0:
            print("La machine abandonne")
            alu = []
            ab = True
        else:
            choix_ia = choice(AI[position])
        choix = choix_ia

    print(f"{choix} allumette(s) retirée(s)")
    position += choix
    if len(alu) > 0:
        for j in range(choix):
            alu.pop()
    if len(alu) == 0 and not i%2:
        print("\nHumain gagnant !!\n")
        alu = [True for i in range(12)]
        AI[position-choix-choix_ia].remove(choix_ia)
        position = 0
    elif len(alu) == 0 and not ab:
        print("\nLa machine gagne\n")
        alu = [True for i in range(12)]
        position = 0
    elif ab:
        alu = [True for i in range(12)]
        position = 0
        ab = False
    print(AI)
    i += 1
