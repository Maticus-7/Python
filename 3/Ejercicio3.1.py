#¿Hay la letra 'a' en el string?XD
string = input("Introduce un string: ")
if 'a' in string:
    print(f"La letra 'a' está presente en el string.")
    for i in range(len(string)):
        if string[i] == 'a':
            print(f"La letra 'a' está en la posición {i}.")
else:
    print("La letra 'a' no está presente en el string.")