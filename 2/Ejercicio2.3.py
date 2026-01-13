#Programa para calcular raíces cuadradas
print('Presentaremos un programa para calcular raíces cuadradas siguiendo el truco de Noether')
print('Cabe aclarar que este truco es muy tosco y no da una aproximación muy buena como la de Newton-Raphson')
numero=float(input('Ingrese el número del cual desea calcular la raíz cuadrada: '))
n=0
while n**2<=numero:
    n+=1
print(n)
if abs(n**2-numero)==min(abs(n**2-numero),abs((n+1)**2-numero)):
    n=n
    print(f'La raíz cuadrada aproximada de {numero} es {n+(numero-n**2)/(2*n)}')
else:
    n=n+1
    print(f'La raíz cuadrada aproximada de {numero} es {n+(numero-n**2)/(2*n)}')


