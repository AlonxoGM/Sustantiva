<<<<<<< HEAD
def ingresar_numero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Error: Debes ingresar un número entero.")

num1 = ingresar_numero("Ingrese el primer número (1 de 3): ")
while True:
    try:
        num2 = int(input("Ingrese el segundo número (2 de 3): "))
        break
    except ValueError:
        print("Error: Debes ingresar un número entero.")

while True:
    try:
        num3 = int(input("Ingrese el tercer número (3 de 3): "))
        break
    except ValueError:
        print("Error: Debes ingresar un número entero.")
if num1 > num2 and num1 > num3:
    print("\nEl número mayor de los tres es:", num1)
elif num2 > num1 and num2 > num3:
    print("\nEl número mayor de los tres es:", num2)
else:
    print("\nEl número mayor de los tres es:", num3)
=======
# Solicita al usuario que ingrese el primer número
num1 = int(input("Ingrese el primer numero (1 de 3):\n"))

# Solicita al usuario que ingrese el segundo número
num2 = int(input("Ingrese el segundo numero (2 de 3):\n"))

# Solicita al usuario que ingrese el tercer número
num3 = int(input("Ingrese el tercer numero (3 de 3):\n"))

# Comprueba si el primer número es el mayor de los tres
if num1 > num2 and num1 > num3:
    print("\nEl numero mayor de los tres es:", num1)
# Comprueba si el segundo número es el mayor de los tres
elif num2 > num1 and num2 > num3:
    print("\nEl numero mayor de los tres es:", num2)
# Si ninguno de los dos casos anteriores se cumple, el tercer número es el mayor
else:
    print("\nEl numero mayor de los tres es:", num3)
>>>>>>> 07ee88b2c08f8541e59529f1df083dac72e6024b
