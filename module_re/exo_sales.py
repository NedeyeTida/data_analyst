import csv, re

donnees_nettoyees = []

def nettoyer_email(email):
    email = re.sub(r"\[at]|\(at\)",'@',email)
    email = re.sub(r"\(dot\)|_", '.', email)
    return email

def nettoyer_prix(prix):
    prix = re.sub(r'[$€eursEUR\s]', '', prix)
    prix = re.sub(r', ', ', ', prix)
    return float(prix)

def nettoyer_date(date) 




file_path = "./module_re/donnees_sales.csv"

import re

with open("./module_re/donnees_sales.csv", 'r', encoding='UTF-8') as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            id, Email, Prix, Date_de_naissance, Telephone =line
            Email-nettoyen = (line(Email)),
            Prix = float[Prix],
            Date_de_naissance = int[Date_de_naissance],
            Telephone = int[Telephone]
            print(line)

