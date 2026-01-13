saldo=float(input('Porfavor ingrese su saldo :'))
if saldo<0:
    print('Usted pidio un prestamo,ahora su saldo es de 10000 dolares.')
    saldo=10000
elif saldo>0 and saldo<=20000:
    print('Usted tiene un saldo positivo,por lo tanto usted pidio un prestamo,ahora su saldo es de 20000 dolares.')
    saldo=20000
else:
    print('Usted tiene un saldo alto,no puede pedir prestamo.')   
insumo=saldo-5000-2000
print(f'Se destinarán {insumo/2} dolares para la compra de insumos e incentivos al personal.')