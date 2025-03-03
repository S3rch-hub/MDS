import re

texto = input()



expresion = r'(?:\d{4}-\d{2}-\d{2})\s(?:\d{2}:\d{2}:\d{2}\.\d{3})\s+(\b(?:INFO|ERROR|DEBUG|WARN)\b)\s+\d+\s+---\s+\[([\w\d]+)]\s+(?:\w+\.)*(\S+)\s+:\s+(.*)'


salida = re.findall(expresion, texto)


for level,thread,class_name,message in salida:
    print(f'"{level}","{thread}","{class_name}","{message}"')