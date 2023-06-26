# try:
# 	# Es un lugar donde
# 	# tu puedes hacer algo 
#     # sin pedir permiso.
# except:
# 	# Es un espacio dedicado  
#     # exclusivamente para pedir perdón.

# la palabra clave reservada try marca el lugar donde intentas hacer algo sin permiso;
# la palabra clave reservada except comienza un lugar donde puedes mostrar tu talento
# para disculparte o pedir perdón.


# La excepción confirma la regla

# try:
#     value = int(input("Ingresa un número natural: "))
#     print ("El recíproco de", value, "es", 1/value)
# except ValueError:
#     print("No se qué hacer con", value)
# except ZeroDivisionError:
#     print("La división entre cero no está permitida en nuestro Universo.")
# except:
#     print('Ha sucedido algo extraño, ¡lo siento!')


# Rastreando las rutas de ejecución

temperature = float(input('Ingresa la temperatura actual:'))

if temperature > 0:
    print("Por encima de cero")
elif temperature < 0:
    print("Por debajo de cero")
else:
    print("Cero")