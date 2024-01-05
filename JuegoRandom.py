import random

def adivinar_numero():
    numero_a_adivinar = random.randint(1, 50)  # Genera un número aleatorio entre 1 y 50
    intentos = 10

    print("¡Bienvenido al juego de adivinar el número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Ingresa tu suposición: "))

        intentos += 1

        if intento < numero_a_adivinar:
            print("Demasiado bajo, ¡intenta con un número más alto!")
        elif intento > numero_a_adivinar:
            print("Demasiado alto, ¡intenta con un número más bajo!")
        else:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break

adivinar_numero()
