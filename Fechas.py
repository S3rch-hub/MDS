import re
from re import findall

expresion = r'\b(\d{4})-(\d{2})-(\d{2})\b'

texto = input()
texto2 = re.sub(expresion, r"\3.\2.\1", texto)
print(texto2)