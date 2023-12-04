# 1
my_dict = {"Mangue", "Raisin", "Fruit de la passion", "Litchi", "Orange"}
print(my_dict)

fruits = {}
fruits["pomme"] = 2
fruits["Mangue"] = 4
print(fruits)

# 2 
mon_dico = {20, 24, 26, 28, 30}
mon_dico["test"] = "Texte lié à test"


# 3
dico_nom = {"Nani":5, "Nono":8, "Nana":11, "Nini": 15, "Nene":18}
print(dico_nom)
dico_nom["Nani"] = 5
dico_nom["Nono"] = 8
dico_nom["Nana"] = 11
dico_nom["Nini"] = 15
dico_nom["Nene"] = 18

total = 0

print(dico_nom.values())
for values in dico_nom.values():
    print(values)
print(f"la moyenne de la classe est : {total / len(dico_nom)}")


#4
words = {"pomme"}