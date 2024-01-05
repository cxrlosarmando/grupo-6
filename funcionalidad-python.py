def multiplicar():
    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        resultado = numero1 * numero2
        print(f"El resultado de la multiplicación de {numero1} y {numero2} es: {resultado}")
    except ValueError:
        print("Por favor, ingresa números válidos.")

# Llamada a la función para multiplicar
multiplicar()
print("caro estuvo aquí jeje")