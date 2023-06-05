#La lista comienza con un corchete abierto y termina con un corchete cerrado;

#¿Cómo cambias el valor de un elemento elegido en la lista?

#Vamos a asignar un nuevo valor de 111 al primer elemento en la lista. Lo hacemos de esta manera:

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.


#Y ahora queremos copiar el valor del quinto elemento al segundo elemento - ¿puedes adivinar cómo hacerlo?

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.


#Se puede acceder a cada uno de los elementos de la lista por separado. Por ejemplo, se puede imprimir:
print(numbers[0]) # Accediendo al primer elemento de la lista.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

# Cualquier elemento de la lista puede ser eliminado en cualquier momento
# esto se hace con una instrucción llamada del (eliminar). Nota: es una instrucción, no una función.

###

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

###

# Puede parecer extraño, pero los índices negativos son válidos, y pueden ser muy útiles.
# Un elemento con un índice igual a -1 es el último en la lista.

numbers = [111, 7, 2, 1]
print(numbers[-1])

numbers = [111, 7, 2, 1]
print(numbers[-2])