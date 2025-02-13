


import re
texto = input()
expresion = r"\b(?:E[- ]?)?\d{4}[- ]?[A-Z]{3}\b"
resultados = re.findall(expresion, texto)
for r in resultados:
    print(r)
