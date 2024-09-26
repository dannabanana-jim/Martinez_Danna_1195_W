print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("W")
print (" ")
#Muestra un mensaje para introducir los numeros
A =  input("Introduce un numero: ")
B =  input("Introduce un numero: ")
C =  input("Introduce un numero: ")
#Declara que los numero debemn  ser enteros
A = int(A)
B = int(B)
C = int(C)
#Si el usuario ingresa valores iguales mostrara un mensaje de que deben ser distintos
if  A == B or B == C or A == C:
    print("Los valores ingresados deben ser distintos")
else:
    mayor = max(A,B,C)
    menor = min(A,B,C)
#Imprime cual es el numero mayor y cual el menor
print("El valor mayor es: ", mayor)
print("El valor menor es: ", menor)

