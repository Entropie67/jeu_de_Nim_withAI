from random import choice
AI = [[1, 2, 3] for i in range(10)]
AI.append([1, 2])
AI.append([1])
alu = [True for i in range(12)]
position = 0
ab = False
def affichage():
    for a in alu:
        if a:
            print(" | ", end="")
        else:
            print("_")

game = True
p = ["Humain", "HALL9000"]
i = 0
while game:
    affichage()
    print(f"\nAu tour de  : {p[i%2]}\n")
    if not i%2:
        choix = int(input(f"\n Votre choix : "))
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
        print(choix_ia)
        print(position-choix)
        AI[position-choix-choix_ia].remove(choix_ia)
        position = 0
        # retirer dernier choix
    elif len(alu) == 0 and not ab:
        print("\nLa machine gagne encore\n")
        alu = [True for i in range(12)]
        position = 0
    print(AI)
    i += 1
