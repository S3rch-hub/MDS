import re
from re import findall

texto = input()

expresion = r'\b(?:C/|Calle)\s([A-Z][a-zA-Z]+)\s(?:[nN]º?)?\s?(\d+),\s+(\d{5})\b'
resultados = re.findall(expresion, texto)

for nombre, numero, codigo in resultados:
    print(codigo, nombre, numero, sep="-")