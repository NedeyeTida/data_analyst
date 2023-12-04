import json, os # JSON -> Javascript Object Notation

file_path = "./demo/file.json"
mon_dict = {"people": ["Toto", "Tata", "Titi"], "object" : ["Ballon", "Ordinateur", "Voiture"]}

if os.path.exists(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:
        #Pur charger un fichier dans un dictionnaire il nou faut la methode .load()
        data = json.load(file)
        print(data)
        
else:
    with open(file_path, "w", encoding="UTF-8") as file:
        #pour sauvegarder un objet/dictionnaire dans JSON, il nous faut la methode.dump()
        #indent sert à avir une présentation plus esthétique
        json.dump(mon_dict, file, indent=4)

#Pour obtenir la variable string qui va être la representation textuelle d'un objet/dictionnaire,
#on peut se servir de la méthode .dumps() qui va retourner une chaine de caracteres.
json_str = json.dumps(mon_dict, indent=4)
print(json_str)
print(type(json_str))


#Pour transformer une chaine de caractere au format JSON en dictionnaire,
#il existe la methode . loads() qui va retourner un dictionnaire
data2 = json.loads(json_str)
print(data2)
print(data2["people"])