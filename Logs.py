import re
from re import findall

texto = input()

expresion = r'(?P<time>\S+)\s+(?P<level>\bINFO\b|\bERROR\b|\bDEBUG\b|\bWARN\b)\s+\d+\s+---\s+\[(?P<thread>[\w\d]+)]\s+(?P<class_name>[\w\.]+)\s+:\s+(?P<message>.*)'
salida = re.findall(expresion, texto)
for time,level,thread,class_name,message in salida:
    print(f'"{level}"," {thread} ","{class_name}","{message}')