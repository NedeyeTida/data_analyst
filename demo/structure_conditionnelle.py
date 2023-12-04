# if else

age = int(input("Quel est votre âge? : "))

if age >= 18 :
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")

# if elif

age = int(input("Quel est votre âge? : "))

if age >= 18 :
    print("Vous êtes majeur")
else:
    print("Vous êtes mineur")


# if imbriqués

a,b = 10,5

if a > 5 :
    print("a est superieur à 5 ")
    if b<3 :
        print("a est superieur à 5 et b est inferieur 3")

age = int(input("Quel est votre age ? : "))

message = "Majeur" if age >= 18 else "Mineur"
print(message)

# operateurs :

a = 5
b = 4

if a > 3 and b < 7:
    print("les 2 conditions sont bonnes")

if a < 3 or b > 7:
    print("l'une des conditions est bonne")


    fruit = "Pomme"


if fruit == "Poire":
    print("C'est une Poire")
elif fruit == "Pomme":
    print("C'est une Pomme")
elif fruit == "Orange":
    print("C'est une Orange")
else:
    print("Je ne sais pas ce que c'est")


    fruits = ["Pomme", "Poire", "Orange", "Kiwi"]

# verification dans un tableau

if fruit in fruits :
    print("C'est une pomme")