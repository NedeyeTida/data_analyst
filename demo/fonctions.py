# print ("hello world")
# fonctions sans paramètres

def hello_world():
    print("Hello world!")


hello_world()
hello_world()
hello_world()


#fonctions avec parmètres 

def bonjour_qui(nom, age):
    print(f"bonjour {nom}, tu as {age}")


bonjour_qui("Christophe", 27)
bonjour_qui("Toto", 30)



def addition(a,b):
    print("Je fait une addition")
    resultat = a + b
    return resultat

resultat = addition(2,3)
print(resultat)


