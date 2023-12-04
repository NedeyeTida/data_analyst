# structure iterative
# for

for i in range(5):
    print("i :", i)

for i in range (3,9): 
    print ("i : ", i)

for i in range (2,9,2): 
    print ("i : ", i)

for i in range (300,200,-2): 
    print ("i : ", i)


 #boucle while:
i = 0
while i < 5:
    print("i : ", i)
    i+=1 

valeur  = input("Donnez la valeur : ")

while valeur == "toto": 
    valeur = input("Donnez la valeur : ") 


for i in range(10):
    if i == 5:
       break
    print("i ", i)

    
for i in range(10):
    if i == 5 :
      continue
    print("i ", i)
 
for i in range(10):
 print("i ", i)
else:
    print("La boucle est terminée") 