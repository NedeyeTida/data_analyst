# import mysql.connector
import pandas as pd
from sqlalchemy import create_engine, text
import openpyxl


df_personnes = pd.DataFrame(
    data=[
        ["Alexandre", "Aabou", "alexandre.aabou@email.com"],
        ["Barbara", "Bernard", "barbara.bernard@email.com"],
        ["Camila", "Caruso", "camila.caruso@email.com"],
        ["David", "Doherty", "david.doherty@email.com"]
    ],
    columns=["prenom", "nom", "mail"]
)


# SQL -------------------------------------------------------------------------------------

# Option 1 : mysql.connector --------------------------------------------------------------

# conn = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='sakila'
# )

# Lecture :

# df_actors = pd.read_sql_query('SELECT actor_id, first_name, last_name FROM actor', conn)

# print(df_actors)

# Écriture :

# Utilisation du .cursor() nécessaire (cf demo_with_csv.py)

# -----------------------------------------------------------------------------------------

# Option 2 : Pandas + SQLAlchemy ----------------------------------------------------------

conn = create_engine('mysql+mysqlconnector://root:root@localhost:3306/sakila')
# conn = create_engine('mysql+mysqlconnector://[user]:[pass]@[host]:[port]/[db]')

# Lecture :

df_actors = pd.read_sql_query('SELECT actor_id, first_name, last_name FROM actor', conn)

print(df_actors)

# Écriture :

df_personnes.to_sql('personne', conn, if_exists='replace', index=False)
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html
# if_exists = 'fail', 'replace' ou 'append, par défaut : 'fail'
# # index=False, ne transforme pas l'index de la dataframe en une colonne SQL

# attention aux mots réservés !

with conn.connect() as con:
    con.execute(text('ALTER TABLE personne ADD id INT PRIMARY KEY AUTO_INCREMENT FIRST;'))
    
# CSV -------------------------------------------------------------------------------------

# Lecture
file_path = "pandas/Salaries.csv"
df_salaries = pd.read_csv('file_path')

# Écriture

df_personnes.to_csv('FichierPersonnes.csv', index=False, header=False, mode='a')
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html
# Rappel sur le mode='w', 'x', 'a' ('w' par défaut) : que faire si le fichier existe
#   'w' : write, on écrase le fichier
#   'a' : append, on ajoute à la suite (dans ce cas, l'option header=False permet de ne pas rajouter le nom des colonnes)
#   'x' : exclusive creation, échoue (FileExistsError)



#Excel---------------------------------------------------------------------------------

#Pour toute les options (sélectionner certaines colonnes header, feuille....)
#feuille de calcul : sheet_name 'Ventes2021' (valeur par défaut : 0 donc la première)
#https://pandas.pydata.org/docs/reference

df_ventes_boutique = pd.read_excel('input output/VentesBoutique.xlsx', sheet_name="Vente2021")

print(df_ventes_boutique)

#ecriture
df_personnes.to_excel('fichiersPersonnes.xlsx', sheet_name='Feuille de calcul 1')

#JSON

#Lecture

df_animaux=pd.read_json('animaux.json')

print(df_animaux)
