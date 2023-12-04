#1-Installation des Dépendances :
"Installez MySQL Connector Python : pip install mysql-connector-python. Assurez-vous que MySQL est installé et fonctionnel sur votre système."


#2- Création de la Base de Données :
"Utilisez MySQL pour créer une base de données et une table de test. Par exemple, une table utilisateurs avec des colonnes id, nom, email."

import mysql.connector, csv

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='bdusers'
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))")

file_path = "./revisions/utilisateurs.csv"

sql = "INSERT INTO users (name, adress) VALUES(%s, %s)"
values = ("Toto", "rue de paris")
mycursor.execute(sql, values) 


mycursor.execute('SELECT *FROM users')

#EXTRAIRE LES DONNEES RECUPEREES DEPUIS LA REQUETE SQL POUR LES METTRE EN FORMAT PYTHON
data = mycursor.fetchall()
print(data)
for values in data:
    print(values)


#3- Fonction de Nettoyage des Données :
"Créez une fonction en Python qui utilise le module re pour nettoyer les données d'entrée (par exemple, retirer les caractères spéciaux). Appliquez cette fonction aux données d'entrée avant de les insérer dans la base de données."








#4- Script Python pour l'Interaction avec la Base de Données :
"Écrivez un script Python qui se connecte à la base de données MySQL. Ajoutez des fonctions pour insérer et lire des données de la table utilisateurs."