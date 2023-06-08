# # La lista comienza con un corchete abierto y termina con un corchete cerrado;

# # ¿Cómo cambias el valor de un elemento elegido en la lista?

# # Vamos a asignar un nuevo valor de 111 al primer elemento en la lista. Lo hacemos de esta manera:

# numbers = [10, 5, 7, 2, 1]
# # Imprimiendo contenido de la lista original.
# print("Contenido de la lista:", numbers)

# numbers[0] = 111
# # Contenido actual de la lista.
# print("Nuevo contenido de la lista: ", numbers)


# # Y ahora queremos copiar el valor del quinto elemento al segundo elemento - ¿puedes adivinar cómo hacerlo?

# # Copiando el valor del quinto elemento al segundo elemento.
# numbers[1] = numbers[4]
# # Imprimiendo el contenido de la lista actual.
# print("Nuevo contenido de la lista:", numbers)


# # Se puede acceder a cada uno de los elementos de la lista por separado. Por ejemplo, se puede imprimir:
# print(numbers[0])  # Accediendo al primer elemento de la lista.

# # Imprimiendo la longitud de la lista.
# print("\nLongitud de la lista:", len(numbers))

# # Cualquier elemento de la lista puede ser eliminado en cualquier momento
# # esto se hace con una instrucción llamada del (eliminar). Nota: es una instrucción, no una función.

# ###

# del numbers[1]  # Eliminando el segundo elemento de la lista.
# # Imprimiendo nueva longitud de la lista.
# print("Longitud de la nueva lista:", len(numbers))
# # Imprimiendo el contenido de la lista actual.
# print("\nNuevo contenido de la lista:", numbers)

# ###

# # Puede parecer extraño, pero los índices negativos son válidos, y pueden ser muy útiles.
# # Un elemento con un índice igual a -1 es el último en la lista.

# numbers = [111, 7, 2, 1]
# print(numbers[-1])

# numbers = [111, 7, 2, 1]
# print(numbers[-2])
# print()


# # Un nuevo elemento puede ser añadido al final de la lista existente:
# # Dicha operación se realiza mediante un método llamado append().
# # Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

# # list.append(value)

# # La longitud de la lista aumenta en uno.

# # El método insert() es un poco más inteligente -
# # puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.

# # list.insert(location, value)

# # Toma dos argumentos:

# # el primero muestra la ubicación requerida del elemento a insertar; nota: todos los elementos existentes que ocupan ubicaciones a la derecha del nuevo elemento (incluido el que está en la posición indicada) se desplazan a la derecha, para hacer espacio para el nuevo elemento;
# # el segundo es el elemento a insertar.

# print("Agregando elementos a una lista: append() e insert()")

# numbers = [111, 7, 2, 1]
# print("tamaño de la lista: ", len(numbers))
# print(numbers)

# ###

# numbers.append(4)

# print("tamaño de la lista: ", len(numbers))
# print(numbers)

# ###

# numbers.insert(0, 222)
# print("tamaño de la lista: ", len(numbers))
# print(numbers)

# # Puedes iniciar la vida de una lista creándola vacía (esto se hace con un par de corchetes vacíos)
# # y luego agregar nuevos elementos según sea necesario.

# my_list = []  # Creando una lista vacía.

# for i in range(5):
#     my_list.append(i + 1)

# print(my_list)

# my_list = []  # Creando una lista vacía con insert().

# for i in range(5):
#     my_list.insert(0, i + 1)

# print(my_list)

# # El bucle for tiene una variante muy especial que puede procesar las listas de manera muy efectiva
# # - echemos un vistazo a eso.

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in range(len(my_list)):
#     total += my_list[i]

# print(total)

# # Pero el bucle for puede hacer mucho más. Puede ocultar todas las acciones conectadas
# # a la indexación de la lista y entregar todos los elementos de la lista de manera práctica.

# # Este fragmento modificado muestra como funciona:

# my_list = [10, 1, 8, 3, 5]
# total = 0

# for i in my_list:
#     total += i

# print(total)

# #Ahora puedes intercambiar fácilmente los elementos de la lista para revertir su orden:
# print("Ahora puedes intercambiar fácilmente los elementos de la lista para revertir su orden: ")

# my_list = [10, 1, 8, 3, 5]
# print(my_list)
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
 
# print(my_list)

# print("Ahora con un bucle for")
# my_list = [10, 1, 8, 3, 5]
# length = len(my_list)
# print(my_list)
# for i in range(length // 2):
#     my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
 
# print(my_list)


# # Ordenando una lista
# print("Ordenando una lista")

# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# print(my_list)
 
# for i in range(len(my_list) - 1):  # necesitamos (5 - 1) comparaciones
#     if my_list[i] > my_list[i + 1]:  # compara elementos adyacentes
#         my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]  # Si terminamos aquí, tenemos que intercambiar elementos.

# print(my_list)
# print()

# # Ordenando una lista
# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.
 
# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]



# # El ordenamiento burbuja – versión interactiva

# my_list = []
# swapped = True
# num = int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list)

# # Función ordenar lista
# my_list = [8, 10, 6, 2, 4]
# my_list.sort()
# print(my_list)

# # También hay un método de lista llamado reverse(), 
# # que puedes usar para invertir la lista, por ejemplo:

# lst = [5, 3, 1, 2, 4]
# print(lst)
 
# lst.reverse()
# print(lst)  # output: [4, 2, 1, 3, 5]

# lst = ["D", "F", "A", "Z"]
# lst.sort()
 
# print(lst)

# # Copiando una lista de la lista

# list_1 = [1]
# list_2 = list_1
# list_1[0] = 2
# print(list_2)

# # Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, 
# # o partes de una lista.
# # En realidad, copia el contenido de la lista, no el nombre de la lista.
# # Esto es exactamente lo que necesitas. Echa un vistazo al fragmento de código a continuación:

# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

# # Copiando la lista completa.
# list_1 = [1]
# list_2 = list_1[:]
# list_1[0] = 2
# print(list_2)

# # Copiando parte de la lista.
# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:3]
# print(new_list)

# Rebanadas - indices negativos

# my_list[start:end]
#start es el índice del primer elemento incluido en la rebanada.
#end es el índice del primer elemento no incluido en la rebanada.

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[1:-1]
# print(new_list)

# Como hemos dicho anteriormente, el omitir el inicio y fin crea una copia de toda la lista:

# my_list = [10, 8, 6, 4, 2]
# new_list = my_list[:]
# print(new_list)


# Más sobre la instrucción del

#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez 
# - también puede eliminar rebanadas:

# my_list = [10, 8, 6, 4, 2]
# del my_list[1:3]
# print(my_list)

# También es posible eliminar todos los elementos a la vez:

# my_list = [10, 8, 6, 4, 2]
# del my_list[:]
# print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list
print(my_list)
