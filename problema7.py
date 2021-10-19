divisor = 1
n = int(input("ingrese un numero"))
while divisor < n:
    resto =n % divisor 
    if resto ==0:
        print(divisor)
    divisor +=1
