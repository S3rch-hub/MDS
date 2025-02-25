import re
from re import findall

expresion = r'\d{4}\-\d{2}\-\d{2}\s'

texto = input()
results = re.findall(expresion, texto)
for r in results:
    print(r)

