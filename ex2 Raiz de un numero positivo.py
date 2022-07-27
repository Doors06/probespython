#Raiz de un numero positivo

import math

n1 = float(input("Ingrese numero positivo:"))

while n1 <= 0:
    n1 = float(input("No es positivo, favor ingresar numero positivo:"))
else: print("La raiz cuadrada de tu numero es: ", math.sqrt(n1))