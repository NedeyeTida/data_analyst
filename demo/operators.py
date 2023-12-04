# les operators

#Operateurs arithmétiques

a,b = 12,60
somme = a + b
print("somme : ", somme)
difference = b - a 
print("difference :", difference)
produit = a * b
print("produit :", produit)
quotient = a / b
print("quotient : ", quotient)
modulo = a % b
print("modulo : ", modulo)
valeur = 15
print("est ce un nombre pair : ", valeur%2==0)
division_entiere = b // a
print("division_entiere :", division_entiere)
exponentiel = a ** b
print("exponentiel", exponentiel)

#Operateurs de comparaison:

a = 5
b = 3 

est_egal = a==b
print("a==b"+ str(est_egal))
est_different = a != b
print("a != b", est_different)
est_inferieur = a<b
print("a < b", est_inferieur)
est_superieur = a>b
print("a>b", est_superieur)
est_inferieur_egal = a<=b
print("a < b", est_inferieur_egal)
est_superieur_egal = a>=b
print("a>b", est_superieur_egal)


#Operateurs logiques:
x = True
y = False

resultat_et = x and y 
resultat_or = x or y 
resultat_not = not x 

#Operateurs d'assignation : 
print("******* Operateurs d'assignation")
a = 6
a = a + 2
a += 2
print("a += 2 " + str(a))
a -= 2
print("a -= 2 " + str(a))
a *= 2
print("a *= 2 " + str(a))
a /= 2
print("a /= 2 " + str(a))
a //= 2
print("a //= 2 " + str(a))




