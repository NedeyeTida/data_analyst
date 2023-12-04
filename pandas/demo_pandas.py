import pandas as pd

annees = [1776, 1867, 1821]

serie1 = pd.Series(data=annees)
print(serie1)
print("premiere data : ", serie1[0])

pays = ["USA", "CANADA", "Mexico"]
serie2 = pd.Series(data=annees, index=pays)

print(serie2)

#print(serie2[0]) déprécié, ne pas faire ça
print(serie2.iloc[0])

print(serie2["USA"])

print("année la plus petite : ", serie2.min())

print(type(serie2))

print("année la plus petite : ", serie2.max())
print("somme des annees : ", serie2.sum())





""" data = {'Produit' : ['Pomme', 'Orange', 'Banane', 'Pasion'],
        'Prix' : [1.00, 0.60, 0.80, 1.20]}
df_fruits = pd.DataFrame(data, index= ['A', 'B', 'C', 'D'])
print(df_fruits)

data = [{'Produit':'Pomme', 'Prix':1.00},
        {'Produit':'Orange', 'Prix':0.60},
        {'Produit':'Banane', 'Prix':0.80},
        {'Produit':'Pasion', 'Prix':1.20},
        {'Produit':'Kiwi'}
        ]
df_fruits = pd.DataFrame(data)
print(df_fruits)

data = [['Pomme', 1.00], ['Banane', 1.20], ['Orange', 0.80], ['Passion', 0.60]]
df_fruits = pd.DataFrame(data)
print(df_fruits) """






# Creer un DataFrame à partir de Series

serieAnnees = pd.Series(data=annees, index=pays, name='Year')
seriePop = pd.Series(data=[328, 38, 126], index=pays, name='Pop')
serieGDP = pd.Series(data=[20.5, 17.1, 1.22], index=pays, name='GDP')


df = pd.DataFrame([serieAnnees, seriePop, serieGDP])
df = df.T #ou df.tranpose()
print(df)

print("_"*50)

#masque, condition

print(df['Pop']>50)

#affichage de la Dataframe filtrée par cette condititon
print(df[df['Pop'] > 50])

print("Pop supéieure à 50 AND NOT Year superieur à 1800")
#
#
""" (Pop supérieure à 50) & ~(Year supérieur à 1800) """
print((df["Pop"] > 50) & ~(df["Year"] > 1800))

print(df[(df["Pop"] > 50) & ~(df["Year"] > 1800)])

#Pour filtrer une liste d'opérations
#Exemple : la population est soit de 328, soit de 38
print(df[df["Pop"].isin([328, 38])])

#
print(df.isnull())
print(df.notnull())
print(df[df.notnull()])

#supprimer les valeurs nulles
df.dropna() #ou df.dropna(axis=0): on supprime les lignes avec les valeurs nulles.
df.dropna(axis=1) #supprime les colonnes avec les valeurs nulles

df.fillna("Nouvelle valeur")
df.fillna(df.mean())

#utilisation df.iloc
# interpolate : voir doc

# GroupBy
# df.groupby("nom_colonne").methode(), voir exercices

print("-"*50)
print("\n--- Utilisation de df.iloc ---")

print("\n• [0] : première ligne (on obtient une série)")
print(df.iloc[0]) 

print("\n• [[0]] : première ligne (on obtient un dataframe)")
print(df.iloc[[0]]) 

print("\n• [[0, 2]] : première et troisième ligne") 
print(df.iloc[[0, 2]]) 

print("\n• [(0, 2)] ou [0, 2] : valeur à la première ligne, 3e colonne") 
print(df.iloc[(0, 2)]) 
print(df.iloc[0, 2]) 

print("\n• [0:2] : de la première ligne (incluse) à la troisième ligne (exclue)") 
print(df.iloc[0:2])

print("\n• Plusieurs lignes, une colonne")
print(df.iloc[0:2, 1])

print("\n• Une ligne, plusieurs colonnes")
print(df.iloc[1, 0:2])

print("\n• Toutes les lignes, plusieurs colonnes")
print(df.iloc[:, 0:2])

print("\n--- Utilisation de df.loc ---")

print("\n• ['USA'] : ligne à l'index USA (Series)")
print(df.loc['USA'])

print("\n• [['USA']] : ligne à l'index USA (DataFrame)")
print(df.loc[['USA']])

print("\n• ['USA']['GDP'] : valeur à la ligne USA, colonne GDP")
print(df.loc['USA']['GDP']) 

print("\n• Plusieurs lignes, une colonne")
print(df.loc['USA':'Mexico', 'Pop'])

print("\n• Changer une valeur")
backup = df.loc['USA']['Year']
df.loc['USA']['Year'] = 9999
print(df.loc['USA'])
df.loc['USA']['Year'] = backup

print("\n• Appliquer une condition")
print(df.loc[df["GDP"]!=20.5])


print("_"*50)
print("\n--- Combinaison de DataFrames ---")

print("Ajout d'une colonne pourcentage : ")
seriePerct = pd.Series(data=["75%, 25% "], index = ["USA", "Mexico"], name = "Perct")
print(seriePerct)
print(pd.concat([df, seriePerct], axis=1))


