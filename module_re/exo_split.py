import re

content = """start line
not
with sTaRt
hello"""


pattern1 = re.compile(r"\n")

lines = re.split(pattern1, content)


demo_str = ["method", "\n", "search from re", "\n", "for life"]

result1 = re.search(pattern, demo_str)

print(result1)



#split --> 
pattern = re.compile(r'\s')
result3 = re.split(pattern, demo_str)

print(result3)