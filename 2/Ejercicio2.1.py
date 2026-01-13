print("Suma de multiplos de 5 cinco comprendido entre A y B")
#Valores
A=float(input("Ingrese el valor de A: "))
B=float(input("Ingrese el valor de B: "))
#Verificación
if A<0:
    A=float(input("A es negativo,por favor ingrese un valor positivo: "))
if B<0:
    B=float(input("B es negativo,por favor ingrese un valor positivo: "))
if B<A:
    print("El valor de A es menor que B, por lo tanto se intercambian los valores")
    A , B = B , A
#Multiplos de 5
suma=0
i=0
while i*5<=B:
    if i*5>=A:
        suma=suma+i*5
    i=i+1
print("La suma de los multiplos de 5 comprendidos entre A y B es: ",suma)
#Comentaurios xddd