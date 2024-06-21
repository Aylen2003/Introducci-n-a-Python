frase = input("Ingrese una frase:")
vocales = ['a','e','i','o','u','A','E','I','O','U']
listaVocales = []
listaConsonantes = []

def vocalesEnFrase(x):
    for letra in x:
        if letra in vocales:
            listaVocales.append(letra)
    print("Vocales: ", listaVocales)

def consonantesEnFrase(x):
    for letra in x:
        if letra not in vocales:
            listaConsonantes.append(letra)
    print("Consonantes: ", listaConsonantes)
