import random


numero_secreto = random.randint(1, 20)

print("¡Bienvenido al juego de adivinanzas!")
print("Intenta adivinar el número secreto (entre 1 y 20). Tienes 7 intentos.")
intentos = 0
max_intentos = 7
adivinado = False

while intentos < max_intentos:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Felicitaciones! ¡Adivinaste el número secreto en {intentos} intento(s)!")
        adivinado = True
        break
    elif intento < numero_secreto:
        print("El número es más grande. ¡Sigue intentando!")
    else:
        print("El número es más pequeño. ¡Sigue intentando!")

if not adivinado:
    print(f"Lo siento, has agotado tus {max_intentos} intentos. El número secreto era: {numero_secreto}. ¡Mejor suerte la próxima vez!")
