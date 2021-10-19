n = int(input("Dame un número : "))
while n <0:
    print("numero incorrecto")
for i in range(1,13):
    resultado = i * n
    print(n, "X", i, " = ", resultado)

