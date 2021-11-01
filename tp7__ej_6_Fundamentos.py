#Tp 7 ej 6: Idem anterior, utilizando busqueda binaria sobre una lista ordenada.
import random

def generarlista(cant):
    lista = []
    for i in range(cant):
        lista.append(random.randint(1,10))
    return lista

def ordenarlista(lista):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                desordenado = True

def busquedabinaria(lista, dato):
    izq = 0
    der = len(lista)-1
    pos = -1
    while izq<=der and pos==-1:
        centro = (izq + der) // 2
        if lista[centro]==dato:
            pos = centro
        elif lista[centro]<dato:
            izq = centro + 1
        else:
            der = centro -1
    return pos

def buscarvalor(lista, dato):
    pos = busquedabinaria(lista, dato)
    if pos==-1:   # Devolvemos una lista vacía si el valor no está presente.
        return []
    # En pos está el valor buscado. Como la lista está ordenada,
    #todas las repeticiones estarán juntas.
    # Vamos a buscar donde comienzan
    i = pos
    while i>0 and lista[i-1]==dato:
        i = i - 1
    inicio = i
    # Ahora vamos a ver donde terminan
    i = pos
    while i<len(lista)-1 and lista[i+1]==dato:
        i = i + 1
    final = i
    # Ya sabemos donde comienta y donde termina. Armamos una lista con un for.
    posiciones = []
    for i in range(inicio, final+1):
        posiciones.append(i)
    return posiciones

# Programa principal
n = int(input("Cantidad de elementos? "))
numeros = generarlista(n)
print("Lista original:")
print(numeros)
ordenarlista(numeros)
print()
print("Lista ordenada:")
print(numeros)
print()
valor = int(input("Elemento a buscar? "))
posiciones = buscarvalor(numeros, valor)
print()
if posiciones == []:
    print("El valor", valor, "no se encontró en la lista")
else:
    print("El valor", valor, "se encontró en las posiciones", posiciones)