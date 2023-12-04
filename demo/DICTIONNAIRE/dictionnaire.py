# Pour créer un dictionnaire
mon_dict = {"clé 1": 1, "clé 2": 4, "Prénom": "Tida"}

# Pour accéder à la valeur liée à la clé d'un dictionnaire, on se sert de la syntaxe :
print(mon_dict["Prénom"])
print(mon_dict["clé 1"])
print(mon_dict)

# Pour ajouter un élément dans un dictionnaire
#          Clé            Valeur
mon_dict["test"] = "Texte lié à test"

# ici on re-affecte la valeur de "clé 1"
mon_dict["clé 1"] = 2

# pour obtenir la liste des clés de notre dictionnaire:
print(mon_dict.keys())
for key in mon_dict.keys():
    print("la clé ->", key)
    print("valeur associée à la clé ->",mon_dict[key])

# Pour obtenir la liste des valeurs de notre dictionnaire:
print(mon_dict.values())
for values in mon_dict.values():
    print(values)

# pour obtenir une liste de tuple avecclés et valeurs
print(mon_dict.items())

for mon_tuple in mon_dict.items():
    cle, valeur = mon_tuple
    print(cle, valeur)

for cle, valeur in mon_dict.items():
    print(cle, valeur)

# pour supprimer une entrée du dictionnaire avec la methode DEL:
del mon_dict["test"] 

# pour supprimer une entrée du dictionnaire avec la methode POP:
mon_dict.pop("clé 1")