print("\n12. Juego de Adivinar con Bucle while ")
numero_secreto =  (ramdon).randint(1, 20) # Elige un número secreto entre 1 y 20
adivinado = False

print("He pensado en un número entre 1 y 20. ¿Puedes adivinarlo?")

while not adivinado:
    try:
        suposicion = int(input("Ingresa tu suposición: "))

        if suposicion == numero_secreto:
            print(f"¡Felicidades! Adivinaste el número secreto que era {numero_secreto}.")
            adivinado = True # Cambia la condición del bucle para que termine
        elif suposicion < numero_secreto:
            print("El número es muy bajo. Intenta de nuevo.")
        else:
            print("El número es muy alto. Intenta de nuevo.")
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número.")