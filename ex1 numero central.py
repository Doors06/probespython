#numero central

n1 = int(input("Ingrese numero 1:"))
n2 = int(input("Ingrese numero 2:"))
n3 = int(input("Ingrese numero 3:"))

if n1<=n2 and n2<=n3:
    print("El Numero central es: ",n2)
elif  n1<=n3 and n3<=n2:
    print("El Numero central es: ",n3)
elif n2<=n1 and n1<=n3:
    print("El Numero central es: ",n1)
elif n2<=n3 and n3<=n1:
    print("El Numero central es: ",n3)
elif n3<=n1 and n1<=n2:
    print("El Numero central es: ",n1)
else: print("El Numero central es: ",n2)