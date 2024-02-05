agenda = {}

def agregar_contacto(nombre):
    if not nombre.isalpha():
        print("Error: El nombre debe contener solo letras del alfabeto.")
        return False
    else:
        print("Nombre válido.")
        return True

def agregar_numero(numero):
    if not numero.isdigit():
        print("Error: El número de teléfono debe contener solo caracteres numéricos.")
        return False
    else:
        print("Número válido.")
        return True

nombre_valido = False
while not nombre_valido:
    nombre = input("Ingrese el nombre del contacto: ")
    nombre_valido = agregar_contacto(nombre)

numero_valido = False
while not numero_valido:
    numero = input("Ingrese el número de teléfono: ")
    numero_valido = agregar_numero(numero)

if nombre_valido and numero_valido:
    agenda[nombre] = numero
    print("Contacto agregado a la agenda:", agenda)
