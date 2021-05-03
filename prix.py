import random
 
n = random.randint(0,100)
commentaire = "?"
while True:
    num = input("Enter a number ")
    num = int(num)
    if num < n :
        commentaire = "too low"
        print(num, commentaire)
 
    else :
        commentaire = "too high"
        print(num, commentaire)
    if num == n:
        commentaire = "Excellent  !"
        print(num, commentaire)
        break
