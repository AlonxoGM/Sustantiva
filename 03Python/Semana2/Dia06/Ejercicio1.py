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
