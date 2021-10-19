contador = 0
primo = 0
n = int(input("ingresar un numero "))
while contador <= n:
    contador += 1
    if n % contador == 0:
        primo += 1
if primo == 2:
    print("PRIMO")
else:
    print("NO PRIMO")
