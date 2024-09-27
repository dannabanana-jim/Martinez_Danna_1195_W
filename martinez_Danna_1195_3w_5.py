#Ejercicio 5: Desarrollar código que lea dos valores que captures, determinar cual de los dos valores es el
#menor y escríbalo. Realizar un algoritmo que sume dos números y desplegarlo
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("W")
print (" ")

print("conoce que numero es menor: ")
#Muestra mensaje al usuario

A = input("Ingresa un numero: ")
B = input("Ingresa otro numero: ")
#Se declara las variables como enteros

A =  int(A)
B = int(B)
#Se ejecuta y muestra que numero es mayor

if  A < B:
    print("El primer numero es Menor")
else:
    print("El segundo numero es Menor")

print (" ")

#Muestra mensaje al usuario
print("Realiza una suma: ")
D =  input("Introduce un numero: ")
E =  input("Introduce un numero: ")
#Declara que los numeros deben ser enteros

D = int(D)
E = int(E)
#Realiza la suma

suma =  D + E
#Muestra el resulatdo de la suma

print ("La suma es: ", suma)
