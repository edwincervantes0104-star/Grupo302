a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

if b == 0 or c == 0:
    print("No se puede dividir entre cero.")
else:
    resultado = a / b / c
    print("El resultado de la división es:", resultado)
