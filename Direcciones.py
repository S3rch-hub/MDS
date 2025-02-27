import re
from re import findall

texto = input()
expresion = r'\b(C\/|Calle)\s[A-Z][a-z]+,?\s{0,}(N|n)?(º)?\d\b'