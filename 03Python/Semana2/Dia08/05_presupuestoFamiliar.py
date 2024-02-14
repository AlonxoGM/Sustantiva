ingresos_mensuales = float(input("Ingrese el total de ingresos mensuales: "))

gastos_mensuales = {}

categorias = ["Alimentación", "Transporte", "Vivienda", "Educación", "Entretenimiento"]

for categoria in categorias:
    gasto = float(input(f"Ingrese el gasto mensual para {categoria}: "))
    gastos_mensuales[categoria] = gasto

total_gastos = sum(gastos_mensuales.values())

print("\nResumen de ingresos y gastos:")
print(f"Ingresos mensuales: ${ingresos_mensuales}")
print(f"Gastos mensuales totales: ${total_gastos}")

saldo_restante = ingresos_mensuales - total_gastos

if saldo_restante >= 0:
    print(f"\n¡Excelente! Su saldo restante es de ${saldo_restante}.")
else:
    print("\nAdvertencia: ¡Ha excedido su presupuesto mensual!")
    print(f"Su saldo restante es de ${saldo_restante}.")

opcion = ""
while opcion.lower() not in ['s', 'n']:
    opcion = input("\n¿Desea solicitar un préstamo en el banco? (s/n): ")
    if opcion.lower() == 's':
        cantidad_prestamo = float(input("Ingrese la cantidad de préstamo que desea solicitar: "))
        print(f"Se ha solicitado un préstamo de ${cantidad_prestamo}.")
    elif opcion.lower() == 'n':
        print("Gracias, tenga en cuenta sus opciones financieras.")
    else:
        print("Opción no válida. Por favor, ingrese 's' para sí o 'n' para no.")

gasto_total = float(input("\nIngrese el gasto mensual total: "))
saldo_restante_nuevo = ingresos_mensuales - gasto_total

if saldo_restante_nuevo >= 0:
    print(f"\n¡Excelente! Su saldo restante es de ${saldo_restante_nuevo}.")
else:
    print("\nAdvertencia: ¡Ha excedido su presupuesto mensual!")
    print(f"Su saldo restante es de ${saldo_restante_nuevo}. Debe revisar sus gastos.")
