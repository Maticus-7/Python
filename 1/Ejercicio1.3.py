from math import sqrt
x=list(range(5))
y=list(range(5))
print("Ingrese 5 puntos (x y):")
for i in range(5):
    x[i]=float(input(f'Ingrese coordenada x del punto {i}: '))
    y[i]=float(input(f'Ingrese coordenada y del punto {i}: '))
puntos2=[]
for i in range(5):x[i]=x[i]-x[0] 
for i in range(5):y[i]=y[i]-y[0]
z=list(range(5))
for i in range(5):z[i]=sqrt(x[i]**2+y[i]**2)
print(z)
print("El punto más cercano al punto 0 es el punto con índice:", z.index(min(z[1:])))

