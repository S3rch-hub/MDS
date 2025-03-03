import re
from re import findall

texto = input()

expresion = r'(?:\S+)\s+(\bINFO\b|\bERROR\b|\bDEBUG\b|\bWARN\b)\s+\d+\s+---\s+\[([\w\d]+)]\s+(?:(?:\w+\.)+)?(\S+)\s+:\s+(.*)'
salida = re.findall(expresion, texto)
for level,thread,class_name,message in salida:
    print(f'"{level}","{thread}","{class_name}","{message}"')