#!/usr/bin/python3

# Programa que muestra números primos en un intervalo

lower = 1   # límite inferior
upper = 500 # límite superior

print("Prime numbers between", lower, "and", upper, "are:")

# recorrer todos los números del intervalo
for num in range(lower, upper + 1):

   # los números primos son mayores que 1
   if num > 1:

       # verificar si tiene divisores
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)