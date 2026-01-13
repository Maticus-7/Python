partida=[08.00,09.43,11.19,12.47,14.00,15.45,19.00,21.45]
llegada=[10.16,11.52,13.31,15.00,16.18,17.55,21.20,23.58]
print('Por favor ingresa una hora en formato HH.MM: ')
hora=int(input('Porfavor igresa la hora(HH): '))
minuto=int(input('Porfavor ingresa los minutos(MM): '))
tiempo=hora+minuto/100
tiempo=[max((tiempo - p),(p-tiempo)) for p in partida]
minimo=min(tiempo)
indice=tiempo.index(minimo)
print(f'La hora de salida mas cercana es {partida[indice]:.2f}')
print(f'La hora de llegada correspondiente es {llegada[indice]:.2f}')