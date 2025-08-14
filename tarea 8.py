nota_numerica = 85

print("\n8. Sistema de Calificaciones 💯")
if nota_numerica >= 90:
    calificacion_letra = 'A'
elif nota_numerica >= 80:
    calificacion_letra = 'B'
elif nota_numerica >= 70:
    calificacion_letra = 'C'
elif nota_numerica >= 60:
    calificacion_letra = 'D'
else:
    calificacion_letra = 'F'

print(f"Tu calificación de {nota_numerica} corresponde a la letra: {calificacion_letra}")