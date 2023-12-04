""" # ### Écrire un programme en python qui affiche les tables de 1 à N. N : est un entier supérieur à 0 saisie par l'utilisateur.

nb_table = int(input("saisir le nombre de tables (>0)"))

while nb_table <=0 :
    nb_table=int(input("Saisie incorrecte ! Saisir le nombre de tables (>0) : "))
for chiffre in range (1,11) : 
    print(f"{chiffre:3}", end=" " )
print("\n" + "_"  * 40)

for table in range (1, nb_table + 1) :
    for chiffre in range (1,11):
        print(f"{table * chiffre :3}", end="_")

    print("\n") """

## EXO POPULATION

population = int(input("Saisir la population : "))
taux_pct =float(input("Saisir le taux en (%) : "))
population_visée = int(input("Saisi population_visée : "))
année = 0
 
while population < population_visée :
population*= 1 + taux_pct/100
année += 1

print(f'la population visée dépasse la population en {année} ans ({population}) ')
