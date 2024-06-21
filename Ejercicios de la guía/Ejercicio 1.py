nota1 = float(input("Ingrese la 1er nota:"))
nota2 = float(input("Ingrese la 2da nota: "))
nota3 = float(input("Ingrese la 3er nota:"))

promedio = (nota1 + nota2 + nota3) / 3

if (promedio >= 7):
    print("El alumno promociono la materia")
elif(promedio >= 4):
    print("El alumno debe rendir final")
else:
    print("El alumno debe recursar la materia")
