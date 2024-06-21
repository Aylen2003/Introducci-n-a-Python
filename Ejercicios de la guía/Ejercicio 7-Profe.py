valor = int(input("Ingres un valor positivo:"))
divisores = [2,3,4,5,6,7,8,9]
listaDivisores = []

for divisor in divisores:
    if valor % divisor == 0:
        listaDivisores.append(divisor)

# Ordeno la lista al final
listaDivisores.sort(reverse = True)
if len(divisores) > 0:
    print("Se encontraon estos divisores:{}",format(listaDivisores))
else:
    print("No se encontraron divisores.")
