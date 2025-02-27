import re
from re import findall

alumnos = r'([a-z])\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es'
profesores = r'([a-z]+)\.([a-z]{2,})@urjc\.es'
texto = input()

matchAlumnos = re.search(alumnos,texto)
matchProfesores = re.search(profesores,texto)
if matchAlumnos:
    inicial,apellido,anio= matchAlumnos.groups()
    print("alumno "+ apellido + " matriculado en "+ anio )
if matchProfesores:
    nombre,apellido= matchProfesores.groups()
    print("profesor "+ nombre+ " apellido "+ apellido)

