#concatenation:
str1 = "chaine1"
str2= "chaine2"
str3 = "chaine3"
str4 = str1 + str2 + str3
print(str4)
print(str1 + "" + str2)
print(str1 , str2)


## concatenation avec entier


mon_entier = 12
ma_chaine = "j'ai "
ma_chaine2 = " ans"

print(ma_chaine + str(mon_entier) + ma_chaine2)

print(ma_chaine,mon_entier,ma_chaine2)

## formatage
# .format
prenom_enfant = "Titouan"
ma_chaine_formatage = ("j'ai {0} ans et je m'appellle {1}".format(mon_entier, prenom_enfant))
print(ma_chaine_formatage)
ma_chaine_formatage2 = (f"j'ai {mon_entier} ans et je m'appelle {prenom_enfant}")
print(ma_chaine_formatage2)


## formatage
# saut à la ligne
chaine = " Ligne1\n Ligne2\n Ligne3\n"
print(chaine)
chaine2 = "\tligne 1\n\tLigne 2\n\tligne 3"
print(chaine2)
chaine3 = "je suis une _\"chaine\""
print(chaine3) 

# decoupage de chaine de caractere :

chaine = "abcdefghi"

print(chaine)
print (chaine[8])
print (chaine[0])
print (chaine[8] + chaine[3])
print (chaine[2:7])
print (chaine[:3])
print (chaine[2:7] + chaine[:3])
print (chaine[2:7] + chaine[5:])

# je peux rajouter des pas
# chaine [ <debut> : <fin> : <pas>]
print (chaine[::2])
print (chaine[::3])
print (chaine[:2:2])

print (chaine[-3:])
print (chaine[:-3])
print (chaine[-5:-2])
print (chaine[::-1])
