#installe numpy --> pip install numpy
import numpy as np

my_list = [1,2,3]

my_ar = np.array(my_list)

print(my_ar)

my_list2 = [[1,2,3],[4,5,6], [7,8,9]]

print(my_list2)

my_ar2 = np.array(my_list2)

print(my_ar2)

#creer un tableau avec arange
print(np.arange(0,10,1))

#creer un tableau avec arange et avec un pas de 2
print(np.arange(0,10,2))

#creer un tableau de zeros
print(np.zeros(5))

#creer un tableau de uns
print(np.ones(5))

#creer un tableau de la forme donnée et le rempllit d'echantillons aléatoires
#entre 0 et 1
print(np.random.rand(2))
print(np.random.rand(5,5))

#.randint --> retourne des nombres entiers aleatoires
my_rand_ar = np.random.randint(1,100,(5,5))


arr = np.arange(0,11)

print(arr)


print(arr[8])


print(arr[1:5])

arr[1:5] = 100
print(arr)

#indexation d'un tableau à 2 dimensions
arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

print(arr_2d[1],[2])

#autre syntaxe
print(arr_2d[1,2])

#obtenir toutes les valeurs à partir d'un index donné
print(arr_2d[:2,1:3])

#selection conditionnelle
#affichr True si la valer est strictement superieur à 4
print(arr > 4)

#afficher le tableau avec uniquement les valeurs superieur à 2
print(arr > 2)

print(arr_2d[arr_2d>20,])

#operation numpy
tab_python = [1,2,3,4,5]
tab_python2 = [5,6,7,8,9]

print(tab_python + tab_python2)

print(arr)
#
print(arr + arr)


print(arr * arr)


print(arr - arr)

#Statistiques sommaires
#
print("Statistiques sommaires")


#
print(arr.sum())


#
print(arr.mean())

#calculer la mediane
print(np.median(arr))

#afficher la plus haute valeur
print(arr.max())

#afficher la plus petite valeur
print(arr.min())

print(arr.count)