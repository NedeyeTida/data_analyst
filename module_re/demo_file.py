import re

with open("./demos/python_re/salaries.txt", 'r', encoding='UTF-8') as reader:
    with open("./demos/python_re/result.txt", 'w', encoding='UTF-8') as writer:
        for line in reader:
            id = re.match(r'\d',line)
            salaire = re.search(r'\d{4,}\.\d{2}', line)
            if salaire:
                print(id.group())
                print(salaire.group())
                writer.write(id.group()+"\t")
                writer.write(salaire.group()+"\n")

           