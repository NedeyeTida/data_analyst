import csv, os

"""
    Un fichiers CSV est une forme courante de stockage de données, ou les valeurs de chaques lignes 
    sont séparés par un caractère spécifique appelé "délimiteur", par défaut le délimiteur est une virgule.
"""

file_path = "./demo/manip_fichiers_csv/annuaire.csv"
mes_donnees = []
if os.path.exists(file_path):
    file = open(file_path, "r", encoding="UTF-8")
    csv_reader = csv.reader(file, delimiter=";")
    for line in csv_reader:
        print(line)
        print(line[0])
        mes_donnees.append(line)
else:
    file = open(file_path, "w", encoding="UTF-8", newline='')
    # On créer un CSV writer pour écrire dans le fichier csv
    csv_writer = csv.writer(file, delimiter=";")
    # Pour ajouter une ligne à notre fichier : 
    csv_writer.writerow(["Toto", "Tata", "Titi"])
    # Pour ajouter plusieurs lignes d'un coup :
    csv_writer.writerows([["blaA", "blaB", "blaC"], ["blaA", "blaB", "blaC"]])
    file.close()

print(mes_donnees)