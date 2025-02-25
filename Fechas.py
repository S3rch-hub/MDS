import re
from re import findall

expresion = r'(\d{4})\-(\d{2})\-(\d{2})\s'

texto = input()
texto2 = re.sub(expresion, r"\3.\2.\1 ", texto)
print(texto2)