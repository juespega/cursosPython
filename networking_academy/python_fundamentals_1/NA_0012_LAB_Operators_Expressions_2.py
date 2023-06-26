hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aquí.
mins = mins + dura  # encuentra el número total de minutos
# encuentra el número de horas ocultas en los minutos y actualiza las horas
hour = hour + mins // 60
mins = mins % 60  # corrige los minutos para que estén en un rango de (0..59)
hour = hour % 24  # corrige las horas para que estén en un rango de (0..23)

print(hour, ":", mins, sep='')
