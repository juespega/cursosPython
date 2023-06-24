# ¿Cómo crear un diccionario?

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
# phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
# empty_dictionary = {}

# print(dictionary)
# print(phone_numbers)
# print(empty_dictionary)


# ¿Cómo utilizar un diccionario?

# El siguiente código busca de manera segura palabras en francés:

# dictionary = {"cat": "gato", "perro": "chien", "caballo": "cheval"}
# words = ['cat', 'león', 'caballo']

# for word in words:
#     if word in dictionary:
#         print(word, "->", dictionary[word])
#     else:
#         print(word, "no está en el diccionario")


# Cuando escribes una expresión grande o larga, puede ser una buena idea mantenerla alineada verticalmente.
# Así es como puede hacer que el código sea más legible y más amigable para el programador, por ejemplo:

# # Ejemplo 1:
# dictionary = {
#     "gato": "chat",
#     "perro": "chien",
#     "caballo": "cheval"
# }
# # Ejemplo 2:
# phone_numbers = {'jefe': 5551234567,
#                  'Suzy': 22657854310
#                  }


# Métodos y funciones de los diccionarios

# El método keys()
# El método retorna o regresa una lista de todas las claves dentro del diccionario

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# for key in dictionary.keys():
#     print(key, "->", dictionary[key])


# El método items()
# Este método retorna una lista de tuplas
# (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas)
# donde cada tupla es un par de cada clave con su valor.

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# for spanish, french in dictionary.items():
#     print(spanish, "->", french)


# Modificar, agregar y eliminar valores

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# dictionary['gato'] = 'minou'
# print(dictionary)


# La función sorted()
# ¿Deseas que la salida este ordenada? Solo hay que agregar al bucle for lo siguiente:

# for key in sorted(dictionary.keys()):
#     pass

# También existe un método denominado values(),
# funciona de manera muy similar al de keys(), pero regresa una lista de valores.

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# for french in dictionary.values():
#     print(french)


# Agregando nuevas claves

# El agregar una nueva clave con su valor a un diccionario es tan simple como cambiar un valor.
# Solo se tiene que asignar un valor a una nueva clave que no haya existido antes.

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# dictionary['cisne'] = 'cygne'
# print(dictionary)

# # También es posible insertar un elemento al diccionario utilizando el método update(), por ejemplo:

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# dictionary.update({"pato": "canard"})
# print(dictionary)


# # Eliminado una clave
# # Esto se logra con la instrucción del.
# # Nota: al eliminar la clave también se removerá el valor asociado.
# # Los valores no pueden existir sin sus claves.

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# del dictionary['perro']
# print(dictionary)

# # Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem():

# dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

# dictionary.popitem()
# print(dictionary)  # salida: {'gato': 'chat', 'perro': 'chien'}


# # Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
# d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
# d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
# d3 = {}

# for item in (d1, d2):
#     d3.update(item)

# print(d3)


# Escribe un programa que convierta la tupla colors en un diccionario.

colors = (("green", "#008000"), ("blue", "#0000FF"))

colors_dictionary = dict(colors)

print(colors_dictionary)

