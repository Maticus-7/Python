#Es primo?
def es_primo(n):
    if n==1:
        return print('El 1 no es primo mi rey')
    for i in range(2,n):
        if n%i==0:
            return print(f'El {n} no es primo')
    return print(f'El {n} es primo')

n=int(input('Ingrese un número para saber si es primo: '))
es_primo(n)