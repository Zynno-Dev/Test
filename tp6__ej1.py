# TP 6, ejercicios 1 
def multiplicar(a, b):
    cont = 0
    total = 0
    while cont<b:
        total = total + a
        cont = cont + 1
    return total



# Programa principal
nro1=int(input("ingrese un valor "))
nro2=int(input("ingrese otro valor "))
print(multiplicar(nro1, nro2))
