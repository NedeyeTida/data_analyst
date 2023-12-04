import json, os # JSON -> Javascript Object Notation

file_path = "./exercices/file.json"
music_list = []

def save():
    with open (file_path, "w", encoding="UTF-8")as file:
        

if os.path.exists(file_path):
    with open(file_path, "r", encoding="UTF-8") as file:
       music_list = json.load(file)
    
        
else:
    save()

#Pour obtenir la variable string qui va être la representation textuelle d'un objet/dictionnaire,
#on peut se servir de la méthode .dumps() qui va retourner une chaine de caracteres.
json_str = json.dumps(mon_dico, indent=4)
print(json_str)
print(type(json_str))


#Pour transformer une chaine de caractere au format JSON en dictionnaire,
#il existe la methode . loads() qui va retourner un dictionnaire
data2 = json.loads(json_str)
print(data2)
print(data2["MENU PRINCIPAL"])