import re
demo_str = 'an apple_a day keeps hte doctor away'

#Ce regex correspondra à toutes les chaines de caractères avec un a suivi de zero
#caracteres alphanumeriques (A-Z, a-z, 0-9)
pattern = re.compile(r'a[\w]*')

result = re.findall(pattern, demo_str)
print(result)

result2 = re.findall(r'\ba[\w]*\b', demo_str)
print(result2)

demo_str2 = "the meeting will be conducted on 1st and 21st of every month"


result3 = re.findall(r'\b\d[\w]*', demo_str2)
print(result3)

