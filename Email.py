import re
from re import findall

alumnos = r'\b([a-z])\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es\b'
profesores = r'\b([a-z]+)\.([a-z]{2,})@urjc\.es\b'
texto = input()


matchAlumnos = re.findall(alumnos,texto)
matchProfesores = re.findall(profesores,texto)
for inicial,apellido,anio in  matchAlumnos:
    print(f"alumno "+ apellido + " matriculado en "+ anio )
for nombre,apellido in matchProfesores:
    print(f"profesor "+ nombre+ " apellido "+ apellido)

