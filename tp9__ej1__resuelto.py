"""TP 9 Ejercicio 1: Leer los números de legajo de los alumnos de un curso y su nota de examen final. Cargar el
número de legajo en la lista LEGAJOS y la nota en la lista NOTA_FINAL. El fin de la carga se
determina ingresando un -1 como legajo. Se debe validar que la nota ingresada sea entre 1 y
10. Terminada la carga de datos, recorrer las listas e informar:
▪ Cantidad de alumnos que aprobaron con nota mayor o igual a 4
▪ Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
▪ Promedio de nota y los legajos que superan el promedio
Luego se solicita, mostrar un listado de legajos y calificaciones ordenadas de manera ascendente según el número de legajo, resolverlo usando listas paralelas."""


def ordenarlistas(listaleg, listanot):
    # Ordenamos las dos listas en paralelo por burbujeo
    desordenado = True
    while desordenado:
        desordenado = False
        for i in range(len(listaleg)-1):
            if listaleg[i]>listaleg[i+1]:
                aux = listaleg[i]
                listaleg[i] = listaleg[i+1]
                listaleg[i+1] = aux
                aux = listanot[i]
                listanot[i] = listanot[i+1]
                listanot[i+1] = aux
                desordenado = True

# Programa principal
listalegajos = []
listanotas = []
aprobar,desaprobar,suma=0,0,0
legajo = int(input("Legajo? (-1 para terminar) "))
while legajo!=-1:
    nota = int(input("Calificación? "))
    while nota<1 or nota>10:
        print("Nota inválida. Debe estar entre 1 y 10.")
        nota = int(input("Calificación? "))
    listalegajos.append(legajo)
    listanotas.append(nota)
    print()
    legajo = int(input("Legajo? (-1 para terminar) "))
print()
for i in range (len(listanotas)):
    if listanotas[i]>=4:
        aprobar=aprobar+1
    else:
        desaprobar=desaprobar+1
    suma=suma+listanotas[i]
if len(listanotas)==0:
    print("no se ingresaron valores")
else:
    prom=suma/len(listanotas)
    print ("La cantidad de alumnos que aprobaron el examen con nota mayor o igual a 4 es ",aprobar)
    print ("La cantidad de alumnos que desaprobaron el examen  con nota menor a 4 es ",desaprobar)
    print ("El promedio de todas las notas es ",prom)
    for i in range(len(listanotas)):
        if listanotas[i]>prom:
            print("Legajo:", listalegajos[i], " -  Calificación:", listanotas[i])

    
#Imprimimos las lista ordenada la lista de legajos ascendentementemte
ordenarlistas(listalegajos, listanotas)
for i in range (len(listalegajos)):
    print ("El numero de legajo del alumno es ",listalegajos[i]," y su nota es ",listanotas[i])


