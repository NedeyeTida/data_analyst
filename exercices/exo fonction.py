""" def identité(prenom, nom) :
    return(prenom + " " + nom) 
resultat = identité("Marisol, DASILVA")
print("resultat")

# soustraction
def soustraction(a,b):
    print(f"Je fait une soustraction {a} et {b}")
    resultat = a - b
    return resultat

resultat = soustraction(36,13)
print(resultat)

#heure
def quelle_heure(heure="12h00") :
    print(f"il est {heure}")

quelle_heure()
quelle_heure("14h00") """

#compter lettre
def compter_lettre_a(chaine):
    count = 0
    for lettre in chaine:
     if lettre == "a":

       return count
    
nb_a = compter_lettre_a ("abba")
print(f'resultat: {nb_a}')

def coompter_lettre_b(chaine):
    return chaine.count('a')