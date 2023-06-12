# # FUNCTIONS

# def message():
#     print("Ingresar valor: ")


# message()
# a = int(input())
# message()
# b = int(input())
# message()
# c = int(input())


# Funciones Parametrizadas

# # También es posible definir funciones con argumentos, como la siguiente que contiene un solo parámetro:

# def hello(name):  # definiendo una función
#     print("Hello,", name)  # cuerpo de la función


# name = input("Ingresa tu nombre: ")
# hello(name)  # invocación de la función

# Recuerda que:
# los parámetros solo existen dentro de las funciones (este es su entorno natural)
# los argumentos existen fuera de las funciones, y son los que pasan los valores
# a los parámetros correspondientes.

# def message(number):
#     print("Ingresa un número:", number)


# message(1)


# def message(what, number):
#     print("Ingresa", what, "número", number)


# message("teléfono", 11)
# message("precio", 5)
# message("número", "number")


# Paso de parámetros posicionales

# def my_function(a, b, c):
#     print(a, b, c)


# my_function(1, 2, 3)


# def introduction(first_name, last_name):
#     print("Hola, mi nombre es", first_name, last_name)


# introduction("Luke", "Skywalker")
# introduction("Jesse", "Quick")
# introduction("Clark", "Kent")


# # Paso de argumentos de palabra clave

# def introduction(first_name, last_name):
#     print("Hola, mi nombre es", first_name, last_name)


# introduction(first_name="James", last_name="Bond")
# introduction(last_name="Skywalker", first_name="Luke")


# Mezclando argumentos posicionales y de palabras clave

# Es posible combinar ambos tipos si se desea - solo hay una regla inquebrantable:
# se deben colocar primero los argumentos posicionales y después los de palabra clave.

# def adding(a, b, c):
#     print(a, "+", b, "+", c, "=", a + b + c)


# adding(1, 2, 3)
# adding(c=1, a=2, b=3)
# adding(3, c=1, b=2)


# Funciones parametrizadas - más detalles

# valores predefinidos

# def introduction(first_name, last_name="Smith"):
#     print("Hola, mi nombre es", first_name, last_name)


# introduction("Jorge", "Pérez")
# introduction("Julián")


# Retornando el resultado de una función

# def happy_new_year(wishes=True):
#     print("Tres...")
#     print("Dos...")
#     print("Uno...")
#     if not wishes:
#         return

#     print("¡Feliz año nuevo!")


# happy_new_year()
# happy_new_year(False)


# return con una expresión

# def boring_function():
#     return 123


# x = boring_function()

# print("La función boring_function ha devuelto su resultado. Es:", x)


# Unas pocas palabras sobre None

# value = None
# if value is None:
#     print("Lo siento, no contienes ningún valor")


# No olvides esto: si una función no devuelve un cierto valor utilizando una cláusula de expresión return,
# se asume que devuelve implícitamente None.

# def strange_function(n):
#     if(n % 2 == 0):
#         return True


# print(strange_function(2))
# print(strange_function(1))


# Efectos y resultados: listas y funciones

# ¿Se puede enviar una lista a una función como un argumento?

# def list_sum(lst):
#     s = 0

#     for elem in lst:
#         s += elem

#     return s


# print(list_sum([5, 4, 3]))


# ¿Puede una lista ser el resultado de una función?

# def strange_list_fun(n):
#     strange_list = []

#     for i in range(0, n):
#         strange_list.insert(0, i)

#     return strange_list

# print(strange_list_fun(5))


# Funciones y alcances

# una variable que existe fuera de una función tiene alcance dentro del cuerpo de la función.

# def my_function():
#     print("¿Conozco a la variable?", var)


# var = 1
# my_function()
# print(var)


# def my_function():
#     var = 2
#     print("¿Conozco a la variable?", var)


# var = 1
# my_function()
# print(var)

"""
Una variable que existe fuera de una función tiene un alcance dentro del cuerpo de la función, 
excluyendo a aquellas que tienen el mismo nombre.

También significa que el alcance de una variable existente fuera de una función 
solo se puede implementar dentro de una función cuando su valor es leído. 
El asignar un valor hace que la función cree su propia variable.
"""

# def my_function():
#     global var
#     var = 2
#     print("¿Conozco a aquella variable?", var)


# var = 1
# my_function()
# print(var)


# Cómo interactúa la función con sus argumentos

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)


my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)
