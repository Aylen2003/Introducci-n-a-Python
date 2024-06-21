numerosEnteros = []
numeroEntero = 1

while not numeroEntero == 0:
    numeroEntero = int(input("Ingrese tantos valores como desee, 0 cero para terminar"))
    if not numeroEntero == 0:
        numerosEnteros.append(numeroEntero)

print("El mayor es {} y el menor es {}.".format(max(numerosEnteros), min(numerosEnteros)))
