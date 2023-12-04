import re

str = (1,5,8,9,5,1,9,5,9,0,5,8,7,1,5,4,5,6,5)

pattern = re.compile("<5>")
print(re.sub(pattern, "cinq", str))





