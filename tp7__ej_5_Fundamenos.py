"""TP 7 Ejercicio 5: Escribir una función para devolver una lista con todas
las posiciones que ocupa un valor pasado como parametro, utilizando busqueda secuencial
en una lista desordenada, La funcion debe devolver una lista vacia si el
elemento no se encuentra en la lista original
"""


def busquedasecuencial(lista2,nro):
    i=0
    listanueva=[]
    while i < len(lista2):
        if lista2[i]==nro:
            listanueva.append(i)
        i=i+1
    return listanueva
    
     
# menu principal
lista2=[4,6,7,4,2,1,19,8,3,0]
print(lista2)
n=int(input("ingrese un valor"))
#busqueda secuencial
listan=busquedasecuencial(lista2,n)
print (listan)