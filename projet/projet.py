import mysql.connector
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import csv

# - En utilisant le fichier cleaned_auto.csv
df = pd.read_csv('projet\cleaned_autos.csv')
print(df)

#Nombre total de véhicules en vente selon le type de véhicule
type_de_véhicule = df.groupby("vehicleType").size().sort_values(ascending=False)
print(type_de_véhicule)
print(df.count())







# Répartition des véhicules en fonction de l'année d'immatriculation