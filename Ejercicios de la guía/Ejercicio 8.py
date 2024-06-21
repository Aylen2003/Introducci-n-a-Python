num1 = int(input("Ingrese un numero:"))
num2 = int(input("Ingrese otro numero:"))
cant = 0 

for numero  in range(num1,num2+1):
    if numero % 2 == 0:
        cant = cant + 1

print("Entre {} y {} se encontraron: {} numeros pares".format(num1,num2,cant))
