import csv 
import os

titre = input("Entrez le titre du prduit : ")
prix = float(input("Entrez le prix du produit : "))
stock = int(input("Entrez le stock du produit : "))

produit = [titre, prix, stock]
file_path = "./exercices/produits.csv"

if os.path.exists(file_path) :
    with open(file_path, "a", newline="", encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(produit)
else:
    with open(file_path, "w", newline="", encoding='UTF-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Titre", "Prix", "stock"])
        writer.writerow(produit)