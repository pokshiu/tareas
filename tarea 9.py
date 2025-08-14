precio_compra = 120

print("\n9. Descuento en Tiendas")
precio_final = precio_compra
if precio_compra >= 100:
    descuento = precio_compra * 0.20
    precio_final = precio_compra - descuento
    print(f"¡Felicidades! Se aplicó un 20% de descuento. Ahorraste {descuento:.2f}€.")
elif precio_compra >= 50:
    descuento = precio_compra * 0.10
    precio_final = precio_compra - descuento
    print(f"¡Felicidades! Se aplicó un 10% de descuento. Ahorraste {descuento:.2f}€.")
else:
    print("No se aplican descuentos.")

print(f"Precio original: {precio_compra}€")
print(f"Precio final: {precio_final:.2f}€")