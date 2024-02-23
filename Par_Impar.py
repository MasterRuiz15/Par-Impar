# Programa para calcular si un numero es PAR o IMPAR

# input
X = int(input("Digite el valor de x: "))

# prossecing
R = (X%2)

if R==0:
    rta= "PAR"

else:
    rta= "IMPAR"

# output
print("El numero " + str(X)  + " es: " + rta)

