import mysql.connector
import re
import numpy as np               #manipulation de tableaux ou calcul mathematiques
import pandas as pd              #analyse de donnees
import seaborn as sns            #visualisation de donnees 
import matplotlib.pyplot as plt  #visualisation les donnees
import matplotlib.cm as cm
import csv 

# - En utilisant le fichier cleaned_auto.csv
df = pd.read_csv('projet\cleaned_autos.csv')
print(df)
print(df.columns)


# #Nombre total de véhicules en vente selon le type de véhicule
type_de_vehicule = df.groupby("vehicleType").size().sort_values(ascending=False)
#type_de_véhicule = df.groupby('vehicleType')['vehicleType'].count().sort_values(ascending=False)
print(type_de_vehicule)
plt.figure(figsize=(12,10))
sns.countplot(x = "vehicleType", data = df)

plt.xlabel('Type de véhicule')
plt.xlabel('Type de véhicule')
plt.ylabel('Nombre de vehicule')

# Ajuster la rotation des étiquettes
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()


# # Répartition des véhicules en fonction de l'année d'immatriculation
vehicule_par_annee = df.groupby('yearOfRegistration').size().sort_values(ascending=False)
print(vehicule_par_annee)
plt.figure(figsize=(12,10))
sns.countplot(x = "yearOfRegistration", data = df)

plt.xlabel('Année enregistrement')
plt.xlabel('Type de véhicule')
plt.ylabel('Nombre de vehicule')

# Ajuster la rotation des étiquettes
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()


# # Nombre de véhicules par marque
vehicule_par_marque = df.groupby('brand')['vehicleType'].count().sort_values(ascending=False)
print(vehicule_par_marque)
plt.figure(figsize=(12,10))
sns.countplot(x = "brand", data = df)

plt.xlabel('Marque')
plt.xlabel('Type de véhicule')
plt.ylabel('Nombre de vehicule')

# Ajuster la rotation des étiquettes
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()


# #Prix moyen des véhicules par type de véhicule et type de boîte de vitesses
prix_moyen_par_type_vehicule = df.groupby(['vehicleType','gearbox'])['price'].mean()
print(prix_moyen_par_type_vehicule)
P1=pd.crosstab(df.vehicleType, df.gearbox)
P1.plot.bar()

plt.xlabel('Boite de vitesse')
plt.xlabel('Type de véhicule')
plt.ylabel('Prix Moyen des véhicules')

# Ajuster la rotation des étiquettes
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()


# #Prix moyen des véhicules selon le type de carburant et le type de boîte de vitesses
prix_moyen_par_type_carburant=  df.groupby(['fuelType','gearbox'])['price'].mean()
print(prix_moyen_par_type_carburant)
P2=pd.crosstab(df.fuelType, df.gearbox)
P2.plot.bar()

plt.xlabel('Boite de vitesse')
plt.xlabel('Type de carburant')
plt.ylabel('Prix Moyen des véhicules')

# Ajuster la rotation des étiquettes
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()


# #Prix moyen des véhicules par type de véhicule et marque
prix_moyen_par_marque = df.groupby(['vehicleType','brand'])['price'].mean().reset_index()
prix_moyen_par_marque = prix_moyen_par_marque.sort_values(by = 'price', ascending=False)
print(prix_moyen_par_marque)
P1=pd.crosstab(df.vehicleType, df.brand)
P1.plot.bar()

plt.xlabel('Marque')
plt.xlabel('Type de véhicule')
plt.ylabel('Prix Moyen des véhicules')

# Ajuster la rotation des étiquettes
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.show()


heatmap = prix_moyen_par_marque.pivot_table(index='brand', columns = 'vehicleType', values = 'price')

# #Créer un heatmap avec Seaborn
plt.figure(figsize=(12, len(heatmap) * 0.3))
sns.heatmap (heatmap, cmap='Greens', annot=True, fmt=".2f", linewidths= 0.5)

plt.xlabel('Marque')
plt.xlabel('Type de véhicule')
plt.ylabel('Moyenne de prix par marque et type de vehicule')

# Ajuster la rotation des étiquettes
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()