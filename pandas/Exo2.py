import pandas as pd

df = pd.read_csv("pandas/Salaries_NaN.csv")
print(df)

#Recuperer les 20 prmiers enegistrements
print(df.head(20))

#Recuperer les 20 prmiers enegistrements
print(df.tail(10))

#Trouver le nombre d'enregistrements de cette dataframe
print(df.count())
print(df.shape) #nombre de lignes et de colonnes
print(len(df)) #len = lenght =taille = longueur

#Quels sont les noms des colonnes
print("colonnes: \n", df.columns)

#Quels types de colonnes
print("type de colonnes : \n", df.dtypes)

#Calculer l'écart-type pour toutes les colonnes numériques
print("ecart-type du salaire : ", df['salary'].std().__round__(2))

#calculer la moyenne des 50 premiers
print("moyenne des 50 premiers: ", df['salary'].head(50).mean().__round__(2))

print(df['salary']>120000)

print(df[df['salary']>120000])


print(df.isnull())

print(df.dropna)