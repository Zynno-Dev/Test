"""Ejercicio 2

Cargar una lista con números ingresados por un usuario hasta que se ingresa un -1
(fin de a carga de los datos) y reemplazar un valor en una posición determinada por el usuario.

Imprimir la lista antes y después del reemplazo."""

def numeros():
    lista = []
    n = 0
    while n != -1:
        n = int(input('Ingrese un número o -1 para terminar: '))
        if n != -1:
            lista.append(n)
    return lista

def imprimirLista(a):
    x = 0
    while x < len(a):
        print(a[x], end=' ')
        x += 1
    print()

def reemplazar(a):
    largo=len(a)
    pos = int(input('Ingrese posición a reemplazar valor: '))
    while pos>len(a)-1 or pos<0:
        pos = int(input('Vuelve a ingresar una posición a reemplazar válida: '))
    val = int(input('Ingrese valor a reemplazar: '))
    a[pos] = val
    return a
    
#Programa Principal
listA = numeros()
imprimirLista(listA)
listB = reemplazar(listA)
imprimirLista(listB)