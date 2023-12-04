import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

data = pd.read_csv("matplotlib/Analyse des Ventes de Jeux Vidéo avec Pandas et Matplotlib.csv")
print(data)

platform = data.groupby("Platform").size()
print(platform)

plt.plot(platform.index, platform)
plt.title("Plateformede jeux videos")
 

plt.xticks(platform.index, rotation="vertical")

#Ajout de ticks principaux
plt.yticks(list(range(0, 1001, 1000)))

#grille principale
plt.grid(color="lightgray") #correspond à which="major"

#grille secondaire
plt.grid(color="lightblue", which='minor')

plt.show()




import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Analyse des Ventes de Jeux Vidéo avec Pandas et Matplotlib.csv')

print(df.isna().sum())

# ventes par région
print(df.columns)
ventes_par_region = df[['NA_Sales','EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()
print(ventes_par_region)

# plt.xticks(rotation='vertical') : pivoter les ticks

# Ventes de jeux de GameBoy par an ######################################################

print(df["Platform"].unique()) # liste les plateformes
ventes_gb = df[df['Platform'] == 'GB'] # on garde uniquement les jeux sur GameBoy
ventes_gb_par_an = ventes_gb.groupby('Year')["Global_Sales"].sum()
plt.plot(ventes_gb_par_an.index, ventes_gb_par_an) # ou ventes_gb_par_an.values
plt.title('Ventes de jeux de GameBoy par an (en millions d\'exemplaires)')
plt.show()














