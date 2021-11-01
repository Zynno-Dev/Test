"""Ejercicio 1
Escribir un programa que utilice funciones para:
Cargar una lista de N elementos con números enteros entre 50 y 780 obtenidos al azar.
El valor de N se ingresa por teclado.
Ordenar la lista en forma ascendente utilizando cualquier método de ordenamiento estudiado.
Pedir un dato al usuario y buscarlo con búsqueda binaria e informar su posición o -1 sino se encuentra.
Luego eliminar de la lista, el valor minimo en todas sus posiciones.
Imprimir por pantalla la lista luego de realizar cada tarea."""

import random

def listarandom():
    x = int(input('Ingrese el tamaño de la lista: '))
    lis = []
    for i in range(x):
        lis.append(random.randint(50,780))
    return lis

def ordenar(a):
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(a) - 1):
            if a[i] > a[i+1]:
                aux = a[i]
                a[i] = a[i+1]
                a[i+1] = aux
                desordenado = True
    return a

def busquedabinaria(v, dato):
    izq = 0
    der = len(v) - 1
    pos = -1
    while izq <= der and pos == -1:
        centro = (izq + der) // 2
        if v[centro] == dato:
            pos = centro
        elif v[centro] < dato:
            izq = centro + 1
        else:
            der = centro - 1
    return pos

def obtenerminimo(a):
    minimo = a[0]
    for i in range(len(a)-1):
        if a[i] < minimo:
            minimo = a[i]
    return minimo

def eliminarminimo(a,b):
    minimo = b
    i = 0
    while i < len(a):
        if a[i] == minimo:
            del a[i]
            i -= 1
        i += 1
    return a

#Programa Principal
a = listarandom()
print(a)
b = ordenar(a)
print()
print('Lista ordenada:')
print(b)
print()
c = int(input('Ingrese dato a buscar: '))
d = busquedabinaria(b,c)
if d == -1:
    print('No se encuentra el dato en la lista')
else:
    print('El dato',c,'se encuentra en la posición',d)
print()
e = obtenerminimo(b)
f = eliminarminimo(b,e)
print('El minimo es',e,'y la lista queda:')
print(f)