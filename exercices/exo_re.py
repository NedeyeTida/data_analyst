import re 

# Exercice 1 : Trouver tous les mots qui commencent par 's'
phrase = "Les sept chaussettes sèches sont si sèches, elles se cassent."

result1 = re.findall(r"\bs[\w]+", phrase)

print(result1)

# Exercice 2 : Trouver tous les mots de trois lettres
phrase = "Cet été, je vais me reposer et lire un bon livre."

result2 = re.findall(r"\b\w{3}\b", phrase)
print(result2)

# Exercice 3 : Trouver toutes les années mentionnées dans le texte
historique = "Les événements de 1848, 1914, 1939 et 2001 sont souvent étudiés en histoire."

result3 = re.findall(r"\b\d{4}\b", historique)
print(result3)

# Exercice 4 : Identifier tous les mots qui finissent par 'ant'
texte = "Le vent soufflant et chantant était apaisant et revigorant."

result4 = re.findall(r"\b\w*ant\b", texte)
print(result4)

# Exercice 5 : Extraire tous les mots qui contiennent deux 'e'
phrase = "Je cherche des exemples pertinents et interessants."

result5 = re.findall(r"\b[a-d,f-z]*e[a-d,f-z]*e[a-d,f-z]*\b", phrase)
print(result5)

# Exercice 6 : Trouver tous les mots avec une lettre répétée (comme "rr" dans "terre")
texte = "Le perroquet parle lettre peu mais pense beaucoup."

result6 = re.findall(r"\b(\w*(\w)\2\w*)\b", texte)
print(result6)

# Plaques d'immatriculation (France : AA-123-AA) :
texte = "Ma plaque d'immatriculation est AA-123-AA."
result7 = re.findall(r"[A-Z]{2}-\d{3}-[A-Z]{2}", texte)
print(result7)


# DateTime (format AAAA-MM-JJ hh:mm:ss) :
texte = "La datetime est  AAAA-MM-JJ hh:mm:ss."
result8 = re.findall(r"\b(20\d{2})-(0[1-9]|1[0-2])-([0-2][0-9]|3[0-1])", texte)
print(result8) 


# Numéros de téléphone (France) :
texte = "Mon numero de elephone est 06-95-91-56-60"
result9 = re.findall(r"\d{2}-\d{2}-\d{2}-\d{2}-\d{2}", texte) 
print(result9)

# Email :



# URLs :