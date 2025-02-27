import re
from re import findall

alumnos = r'\b([a-z])\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es\b'
profesores = r'\b([a-z]{2,})\.([a-z]{2,})@urjc\.es\b'
texto = input()

matchAlumnos = re.search(alumnos,texto)
matchProfesores = re.search(profesores,texto)
if matchAlumnos:
    inicial,apellido,anio= matchAlumnos.groups()
    print("alumno "+ apellido + " matriculado en "+ anio )
if matchProfesores:
    nombre,apellido= matchProfesores.groups()
    print("profesor "+ nombre+ " apellido "+ apellido)

