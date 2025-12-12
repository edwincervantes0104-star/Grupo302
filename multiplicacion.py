# Programa completo para multiplicar tres números

def main():
    print("=== Multiplicación de tres números ===")

    # Pedir valores al usuario
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    # Realizar la multiplicación
    resultado = num1 * num2 * num3

    # Mostrar el resultado
    print("El resultado de la multiplicación es:", resultado)

# Ejecutar el programa
if __name__ == "__main__":
    main()
