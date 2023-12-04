#### exo1
# Créez une liste contenant les nombres de 1 à 10
meu_listo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(meu_listo)

#Ajoutez le nombre 11 à la fin de la liste
meu_listo.append(11)
print(meu_listo)

#Supprimez le nombre 3 de la liste
meu_listo.remove(3)
print(meu_listo)

#Accédez au deuxième élément de la liste
print(meu_listo[1])


#### exo2
# Créez une liste de nombres de 1 à 5
liste = [1, 2, 3, 4, 5]
print(liste)

# Utilisez une boucle pour afficher chaque nombre de la liste
for element in liste:
    print(element)

# Ajoutez 5 à chaque nombre de la liste en utilisant une boucle
for element in liste:
    index = liste.index(element)
    liste[index] += 5

#Afficher la liste mise à jour
print(liste)
    

#### EXO 3
#Créez une liste de nombres non triés
Listes = [12, 2, 5, 11, 7, 8, 3, 10, 6, 1, 4, 9]

#  Inversez l'ordre de la liste triée
Listes.sort()

#  Inversez l'ordre de la liste triée
Listes.sort(reverse=True)

#Ajoutez un nouveau nombre à la liste
Listes.append(8)

#Supprimez le troisième nombre de la liste
Listes.pop(2)

#Affichez la liste mise à jour
print(Listes)


#### exo 4
fruits = ["Mangue", "Raisin", "Figue", "Kiwi"]
#Afficher la liste de fruits disponibles
for fruit in fruits:
    print(fruits)   
#Demander au client quel fruit il désire acheter
client = input("Quel fruit desirez-vous : ")

#Vérifier si le fruit est présent dans le tableau fruits
if client in fruits : 
    print("le fruit est présent") 
    fruits.remove(client)
else:
    print("le fruit n'est pas présent")

#Afficher à nouveau la liste de fruits disponibles
print(fruits)


#### Exo5
#Créez deux listes de nombres
list1 = [5, 10, 8, 4]
list2 = [1, 3, 54, 87]

#Concaténez ces deux listes en une seul
list1.extend(list2)

#Trier la liste obtenue par ordre croissant
