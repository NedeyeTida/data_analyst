import re

# L'expression m\w\w recherche un 'm' dans la chaîne de caractères 
# et vérifie grace aux \w qu'il y ai bien 2 caractères alphanumérique
# \w --> (A à Z et 0 à 9)
# flags IGNORECASE --> Les lettres majuscules et minuscules sont traîter de la même manière
pattern = re.compile(r"m\w\w")

demo_str = "method search fromre"

# Retourne le premier élément trouvé ou None
result1 = re.search(pattern, demo_str)

print(result1.group())

# match -> renvoie la chaîne de caractère trouvée au DEBUT de la chaîne
result2 = re.match(pattern, demo_str)

print(result2)

#  split -> permet d'envoyer une collection de données en fonction du pattern
# \s -> correspond à un espace 
pattern = re.compile(r'\s')
result3 = re.split(pattern, demo_str)

print(result3)

# sub -> rechercher un mot donné et le remplacer par un autre
str2 = "Bonjour <tExt>, test <text>"
pattern = re.compile("<text>", flags=re.IGNORECASE)
# pattern = re.compile("<text>", flags=re.IGNORECASE, 1)
print(re.sub(pattern, "text", str2))

# findall -> extrait la totalité des éléments
result4 = re.findall(r'm\w\w', demo_str)
print(result4)