#Separador de palabras
n=0
palabras=[]
string=input("Ingrese una frase: ")
for i in range(len(string)):
    if string[i]==" ":
        palabras.append(string[n:i])
        n=i+1
palabras.append(string[n:])

#La misma secuencia de palabras, pero en orden contrario.
print("Frase en orden inverso:")
printinv=""
for i in range(len(palabras)-1,-1,-1):
    printinv=printinv+"_"+palabras[i]
print(printinv)