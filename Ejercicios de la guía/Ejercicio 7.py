num = int(input("Ingresa un número entero mayor que cero: "))
divisores = []

for i in range(2, 10):
    if num % i == 0:
        divisores.append(i)

if len(divisores) > 0:
    divisores.sort(reverse=True)
    print("Lista de divisores encontrados (de mayor a menor):", divisores)
else:
    print("No se encontraron divisores exactos.")
