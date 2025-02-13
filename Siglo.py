import re
from re import findall

expresion = r'\b[0-9]{4}\b'

texto = input()
results = re.findall(expresion, texto)
for r in results:
    print(r)