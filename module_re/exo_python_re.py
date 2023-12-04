import re

pattern = re.compile(r"0xB 0", flags=re.IGNORECASE)

demo_str = "method search from re"


result1 = re.search(pattern, demo_str)

print(result1)

result2 = re.match(pattern, demo_str)

print(result2)