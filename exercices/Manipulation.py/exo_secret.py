import os 

def menu():
    while True:
        print("""faites votre choix:
              1.Voir le secret
              2.Modifier le secret
              3.Quitter le programme""")
        choix = input("Votre choix (1|2|3)")

        if choix in "1,2,3":
            return choix
        else:
            print("Erreur, réessayer ! \n\n")

def lire_fichier(path):
    file  = open(path, "r", encoding="UTF-8")
    texte_fichier = file.read()
    file.close()
    return texte_fichier

def ecrire_fichier(path,texte):
    file = open(path, "w", encoding="UTF-8")
    file.write(texte)
    file.close()

def main():
    secret_path = "./exo/secret.txt"

    if os.path.exists(secret_path):
        secret = lire_fichier(secret_path)
    else:
        secret = input("Le secret n'existe pas: Veuillez saisir un premier secret ")

    while True:
        choix = menu()

        match choix :
            case "1":
                print("Voici le secret : " )
                print(secret)

            case "2":
                secret = input("Veuillez saisir le nouveau secret : ")

            case "3" : 
                print("On quitte le programme ! Donc on sauvegarde le secret !")
                ecrire_fichier(secret_path, secret)
                break #sortie de la boucle while

main()