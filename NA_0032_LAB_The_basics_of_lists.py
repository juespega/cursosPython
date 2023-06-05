"""
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
escribir una línea de código que elimine el último elemento de la lista (Paso 2)
escribir una línea de código que imprima la longitud de la lista existente (Paso 3).
"""

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list[2] = int(input(']Ingrese un número: '))
print(hat_list)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[4]

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("El tamaño de la lista es: ", len(hat_list))

print(hat_list)


# Un nuevo elemento puede ser añadido al final de la lista existente:
# Dicha operación se realiza mediante un método llamado append(). 
# Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

#La longitud de la lista aumenta en uno.

#El método insert() es un poco más inteligente - 
# puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.