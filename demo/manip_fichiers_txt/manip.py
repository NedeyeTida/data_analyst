file_path = "./demo/manip_fichiers_txt.txt/fichier.txt" 
file=open(file_path,"r", encoding="utf-8")
print(file.read())

file = open (file_path , "a", encoding="UTF-8")
file.write