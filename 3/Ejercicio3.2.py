#Función de cambio de grados
def cambiar_centigrados_fahrenheit(centigrados):
    fahrenheit = (centigrados * 9/5) + 32
    return fahrenheit
#Tabla del 0 al 100
tabla=[]
for i in range(101):  # 0..100 inclusive
    tabla.append([i, cambiar_centigrados_fahrenheit(i)])
print(tabla)