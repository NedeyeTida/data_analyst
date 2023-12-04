# on crée une liste avec des crochets
ma_liste = [1,2,"test", True, ["a", True, 25]]

print(ma_liste)

# afficher un element de la liste (elle commence TOUJOURS à l'index 0)
print(ma_liste[1])

#afficher plusieurs element de la liste
print(ma_liste[1:4])
print(ma_liste[:4])
print("ici")
print(ma_liste[1::3])

# si on veut afficher un element de la liste contenue dans la première
print(ma_liste[4][1])

# modifier un element à un index precis
# ma_liste [6] = "test"
ma_liste[3] = 5
print(ma_liste)

numbers = [1, 5, 8, 2, 3]

#pour trier une liste on utilise la methode .sort()
# numbers.sort()
numbers2 = sorted(numbers)
print(numbers2)
numbers2.sort(reverse=True)
print(numbers2)

# Pour ajouter à la fin de la liste, on peut utiliser la methode .append()
ma_liste.append(30)
print(ma_liste) 

# Pour ajouter à un index precis, on utilise la methode .insert(index, element)
ma_liste.insert(2, 60)
print(ma_liste)

# Pour ajouter une liste à la fin de la liste.extend()
ma_liste.extend(["Test", 5, True])
print(ma_liste)

# /!\ si on utilise append, on ajoutera un élément de type liste
ma_liste.append(["Test", True])
print(ma_liste)

# Pour retirer un element avec son index 
ma_liste.pop(3)
print(ma_liste)

# pout retirer un element à l'aide de son contenu( la premiere qui correspon)
ma_liste.remove(30)
print(ma_liste)


for element in ma_liste:
    print(element)

for element in ma_liste:
    print("element : ", element)
    print("son index : ", ma_liste.index(element))

    #afficher l'index d'un element precis 
    print(ma_liste.index(5))