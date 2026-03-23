#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

lower = 1 # Numero desde el cual se buscan primos
upper = 500 # Numero hasta el que se buscan los primos

print("Archivo Editado.")
print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than lower (1)
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
