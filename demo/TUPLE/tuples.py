def recuperer_nombre_et_carre(nombre):
    return nombre, nombre**2 #tuple packing -> on se sert d'un tuple pour retourner plusieurs valeurs

print(recuperer_nombre_et_carre(3))
      
# Pour déclarer un tupl, on utilise la syntaxe entre parenthèse
tuple1 = (1, 2, 3, 4, 5)
# ou simplement on séparer les éléments avec une virgule
tuple2 = 1, 2, 3, 4, 5

# Unpacking -> on 'découpe' notre tupe dans plusieurs variables
nombre, carre = recuperer_nombre_et_carre(4)
print("mon nombre : ", nombre)
print("mon nombr au carré : ", carre)

#
var1, _, var3, _, var5 = tuple1

_, carre2 = recuperer_nombre_et_carre(4)
print(carre2)