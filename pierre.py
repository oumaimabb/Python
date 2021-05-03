 from random import choice
 
 
coup = ("Pierre", "Feuille", "Ciseaux")
 
 
while input("Vous voulez jouer ?  (y/n): ").lower() != "n":
 
    print("\n")
    print("Le jeu du: Pierre - Feuille - Ciseaux")
 
    a = int(input("Choisissez un chiffre  :\n0: Pierre\n1: Feuille\n2: Ciseaux\n-> "))
    b = choice(range(3))
 
    print("\n{} VS {}".format(coup[a], coup[b]))
    if a == b:
        print("Tight \n")
    elif (a>b and b+1 == a) or (a<b and a+b == 2):
        print(" Vous avez gagnez *-*.\n")
    else:
        print("Vous avez perdu *_*.\n")
else:
    print("Au revoir.")
