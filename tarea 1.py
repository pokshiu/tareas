coste_comida = 85.50  # Coste de la comida en euros
porcentaje_propina = 0.15 # 15% de propina
propina = coste_comida * porcentaje_propina
total_a_pagar = coste_comida + propina

print(f"\n1. Calculadora de Propinas ")
print(f"Costo de la comida: {coste_comida}€")
print(f"Porcentaje de propina: {porcentaje_propina * 100}%")
print(f"Monto de la propina: {propina:.2f}€")
print(f"Total a pagar: {total_a_pagar:.2f}€"