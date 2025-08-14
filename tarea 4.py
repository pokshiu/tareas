print("\n4. Verificador de Mayoría de Edad ")
try:
    año_actual = 2025
    año_nacimiento = int(input("Ingresa tu año de nacimiento para saber si eres mayor de edad: "))
    edad_calculada = año_actual - año_nacimiento
    es_mayor_de_edad = edad_calculada >= 18 # Variable booleana

    if es_mayor_de_edad:
        print(f"Tienes {edad_calculada} años. Eres mayor de edad.")
    else:
        print(f"Tienes {edad_calculada} años. Eres menor de edad.")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número válido para el año.")