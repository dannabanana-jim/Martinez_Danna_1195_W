#Ejercicio 10: Factorial de un número entero 
print (" ")
print("Danna Paola Martinez Jimenez")
print("no. de control: 1195")
print("W")
print (" ")
# Solicitar al usuario un número entero
n = int(input("Ingresa un número: "))

# Inicializamos la variable 'fact' para almacenar el factorial, comenzando en 1
fact = 1

# Inicializamos el contador 'i' para recorrer desde 1 hasta 'n'
i = 1

# Usamos un ciclo while para calcular el factorial
# Mientras i sea menor o igual a 'n', multiplicamos 'fact' por 'i' y aumentamos 'i' en 1
while i <= n:
    fact *= i  # Multiplicamos el valor actual de 'fact' por 'i'
    i += 1     # Incrementamos 'i' en 1 para continuar el ciclo

# Imprimimos el resultado final del factorial
print(fact)
