import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


# Charger le dataset avec Pandas
data = pd.read_csv('pandas/Étude des Accidents de la Route avec Python et Pandas.csv', dtype={'accident_index': 'str', 'accident_reference': 'str'})

print("nb total de collisions : ", data.shape[0])

# convertir la colonne 'date' en format datetime
# https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html
data['date_formatee'] = pd.to_datetime(data['date'], format="%d/%m/%Y")
print(data['date_formatee'].dt.strftime("%d/%m/%Y"))
# http://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.strftime.html


# Question 1 : Zones à risque

# Plusieurs possibilités

# Par district
accidents_par_district = data.groupby('local_authority_ons_district').size().rename("Nombre d'accidents par district").sort_values(ascending=False)
print(accidents_par_district)
# Voir le fichier data-guide-2022.xlsx pour savoir à quoi correspondent les codes de districts

# Utilisation de 'latitude' et 'longitude' pour identifier les endroits les plus dangereux
accidents_par_coordonnees = data.groupby(['latitude', 'longitude']).size().sort_values(ascending=False).head(3)
print(accidents_par_coordonnees)

# Lower Layer Super Output Areas (LSOA)
accidents_par_lsoa = data.groupby(['lsoa_of_accident_location']).size().sort_values(ascending=False)[1:4]
# [1:4] : On exclut la 1e ligne, celle des données manquantes
print(accidents_par_lsoa)

# Autres possibilités : easting/northing, rural or urban...

# Question 2 : Tendances
# Identifier les jours de la semaine et les heures de la journée avec le plus d'accidents

print("\nLes jours de la semaine avec le plus d'accidents sont :")
print(data['day_of_week'].value_counts())

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
data['day_name'] = data['day_of_week'].replace(list(range(1,8)), week)
print(data['day_name'].value_counts())

data['hour'] = data['time'].str[:2].astype('int')

print("\nLes heures de la journée avec le plus d'accidents sont :")
print(data.groupby('hour').size().sort_values(ascending=False))

""" # Accidents mortels

accidents_mortels = data[data['accident_severity'] == 1]
print("Nombre d'accidents mortels : ", len(accidents_mortels))

print("\nAccidents mortels par conditions météorologiques :")
print(accidents_mortels['weather_conditions'].value_counts())
# weather_conditions	1	Fine no high winds
# weather_conditions	2	Raining no high winds
# weather_conditions	3	Snowing no high winds
# weather_conditions	4	Fine + high winds
# weather_conditions	5	Raining + high winds
# weather_conditions	6	Snowing + high winds
# weather_conditions	7	Fog or mist
# weather_conditions	8	Other
# weather_conditions	9	Unknown
# weather_conditions	-1	Data missing or out of range

# Les jointures
# import du fichier lsoa avec les noms
lsoa = pd.read_csv('pandas/Étude des Accidents de la Route avec Python et Pandas.csv')

# méthode merge
merged = data.merge(lsoa,how='inner',left_on='lsoa_of_accident_location', right_on='LSOA21CD')
# pareil que :
# merged = pd.merge(data,lsoa,how='inner',left_on='lsoa_of_accident_location', right_on='LSOA21CD')
# how : 'inner' (ou left, right, outer...) INNER JOIN (par défaut)
# Définir sur quelle colonne on fait la jointure :
# on : la colonne porte le même nom sur les deux tables (ex on='client_id')
# ici : les colonnes ne portent pas le même nom dans les deux tables
# left_on : nom de la colonne dans la table de gauche (ici, data), right_on : nom de la colonne dans la table de droite (ici, lsoa)

print(merged.columns)

accidents_par_lsoa_2 = merged.groupby(['LSOA21NM']).size().sort_values(ascending=False)
# 'LSOA21NM' : la colonne de lsoa et de merged qui contient les noms des lsoa
print(accidents_par_lsoa_2)
# on remarque qu'on n'a plus la valeur -1
# pas de correspondance de "-1" dans la table lsoa, les lignes avec -1 n'ont donc pas été conservées par l'inner join """


""" nb_collisions = data.shape[0]
data_visualisation = data.groupby('hour').size().sort_values(ascending=False)
print(data_visualisation)
plt.plot(data['hour'], data_visualisation["collisions"])
plt.xticks(data_visualisation['hour'], minor=True)
plt.yticks(data_visualisation['hour'][data_visualisation.index % 2 == 0])
plt.grid(color="lightgray", linewidth=0.5, which="major")
plt.grid(color="indigo", linewidth=0.5, which="minor")

plt.show() """
#visiualisaton

#
#
""" collisions_par_heure = data.groupby('hour').size()

#creation graphique
plt.plot(collisions_par_heure.index, collisions_par_heure)
plt.xlabel("Heure")
plt.ylabel("Nombre d'accidents")
plt.title(f"Accidents par heure en 2022 au Royaume-Uni\nTotal : {collisions_par_heure.sum()} collisions")

#les ticks (graduations) que matplotlib a choisi d'afficher 

plt.xticks(collisions_par_heure.index)

#Ajout de ticks principaux
plt.yticks(list(range(0, 10001, 1000)))

#Ajout de ticks secondaires
plt.yticks(list(range(0, 10001, 500)), minor=True)


#grille principale
plt.grid(color="lightgray") #correspond à which="major"

#grille secondaire
plt.grid(color="lightblue", which='minor')

plt.show() """



accidents_par_gravite = data.groupby('accident_severity').size()

plt.bar(accidents_par_gravite.index, accidents_par_gravite, color=['red', 'orange', 'chartreuse'])
plt.title("Accidents de la route par gravité")
plt.xlabel("Nombre d'accidents")
plt.ylabel("Gravité")

texte = "Gravité : \n 1. Mortel \n 2. Grave \n 3. Léger"
plt.text(1, 60000, texte, bbox=dict(boxstyle="square", edgecolor = "lightblue", facecolor = "#ffffff"))

plt.grid(color="lightgray", linestyle="dotted", axis="y")

plt.show()