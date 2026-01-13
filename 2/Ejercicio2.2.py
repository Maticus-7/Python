tiempo=list(range(10))
valor=0
for i in range(10):
    tiempo[i]=float(input(f"Tiempo en minutos de la prueba {i+1}: "))
    if tiempo[i]>16:
        valor=valor+1
prom=sum(tiempo)/len(tiempo)
if valor==0:
    print('No tuvo pruebas con tiempo mayor a 16 minutos. Aceptado')
elif valor==1:
    print('Tuvo una prueba con tiempo mayor a 16 minutos. Aceptado con observación')
elif valor>1: 
    print('Tuvo más de una pruebas con tiempo mayor a 16 minutos. Rechazado')
elif prom<=15:
    print(f"El promedio de tiempo es {prom} minutos. Aceptado")
else:
    print('No cumplió con los requisitos. Rechazado')