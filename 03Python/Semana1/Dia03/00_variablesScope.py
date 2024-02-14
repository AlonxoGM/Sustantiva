def main():
    num_notas = int(input("Ingrese la cantidad de notas a ingresar: "))

    notas = []

    for i in range(num_notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    promedio = sum(notas) / num_notas

    notas_mayores_al_promedio = sum(1 for nota in notas if nota > promedio)

    print(f"El promedio de las notas es: {promedio}")
    print(f"La cantidad de notas ingresadas que son mayores que el promedio es: {notas_mayores_al_promedio}")

if __name__ == "__main__":
    main()
