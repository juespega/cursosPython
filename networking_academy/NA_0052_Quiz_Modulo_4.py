"""
Pregunta 1

¿Cuál de las siguientes líneas inicia correctamente una definición de función sin parámetros?

def fun():

"""

"""
Pregunta 2
Pregunta de opción múltiple
Una función definida de la siguiente manera:  (Elegir dos respuestas)

+ puede ser invocada sin ningún argumento.
+ puede ser invocado con exactamente un argumento.
"""

# def function(x=0):
#     return x


# print(function(3))


"""
Pregunta 3

Una función integrada es una función que:

viene con Python, y es una parte integral de Python


Pregunta 4

El hecho de que las tuplas pertenezcan a tipos de secuencia significa que:

se pueden indexar y rebanar como las listas
"""

"""
Pregunta 5

¿Cuál es la salida del siguiente fragmento de código?

6
"""

# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x - 1)


# print(f(3))


"""
Pregunta 6

¿Cuál es la salida del siguiente fragmento de código?

4
"""

# def fun(x):
#     x += 1
#     return x


# x = 2
# x = fun(x + 1)
# print(x)


"""
Pregunta 7
Pregunta de opción múltiple
¿Qué código insertarías en lugar del comentario para obtener el resultado esperado?

Salida esperada:

a
b
c
"""

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     #insert your code here
#     print(k[0])


"""
Pregunta 8

El siguiente fragmento de código:

es erroneo
"""


# def func(a, b):
#     return a ** a


# print(func(2))


"""
Pregunta 9

El siguiente fragmento de código:

dará como salida 16
"""


# def func_1(a):
#     return a ** a


# def func_2(a):
#     return func_1(a) * func_1(a)


# print(func_2(2))


"""
Pregunta 10
Pregunta de opción múltiple
¿Cuál de las siguientes líneas inicia correctamente una función utilizando dos parámetros,
ambos con valores predeterminados de cero?

def fun(a=0, b=0):
"""

"""
Pregunta 11

¿Cuáles de las siguientes afirmaciones son verdaderas? (Selecciona dos respuestas)

El valor None puede ser asignado a variables.
El valor None puede ser comparado con otras variables.
"""


"""
Pregunta 12

¿Cuál es la salida del siguiente fragmento de código?

2
"""


# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2)) + 1)


"""
Pregunta 13

¿Cuál es la salida del siguiente fragmento de código?

4
"""


# def fun(x):
#     global y
#     y = x * x
#     return y


# fun(2)
# print(y)


"""
Question 14

¿Cuál es la salida del siguiente fragmento de código?

21
"""


# def any():
#     print(var + 1, end='')


# var = 1
# any()
# print(var)


"""
Pregunta 16

¿Cuál es la salida del siguiente fragmento de código?

no hay salida, el fragmento es erroneo
"""

# my_list = ['Mary', 'had', 'a', 'little', 'lamb']


# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'


# print(my_list(my_list))


"""
Pregunta 17

¿Cuál es la salida del siguiente fragmento de código?

9
"""


# def fun(x, y, z):
#     return x + 2 * y + 3 * z


# print(fun(0, z=1, y=3))


"""
Pregunta 18

¿Cuál es la salida del siguiente fragmento de código?

4
"""


# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2))


"""
Pregunta 19

¿Cuál es la salida del siguiente código?

two
"""

# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)


"""
Pregunta 20

¿Cuál es la salida del siguiente código?

2
"""

# tup = (1, 2, 4, 8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)


"""
Pregunta 21

Selecciona las sentencia true sobre el bloque try-except en relación con el siguiente ejemplo.
(Selecciona dos respuestas).

try:
    # Algo de código...
except:
    # Algo de código...


+ Si existe un error de sintaxis en el código ubicado en el bloque try,
la sentencia except no lo manejará, y una excepción SyntaxError será generada.

+ Si sospechas que un fragmento de código puede generar una excepción,
se debe colocar dentro del bloque try.
"""

"""
Pregunta 22

¿Cuál es la salida del siguiente código?
"""

# try:
#     value = input("Ingresa un valor: ")
#     print(value/value)
# except ValueError:
#     print("Entrada incorrecta...")
# except ZeroDivisionError:
#     print("Entrada errónea...")
# except TypeError:
#     print("Entrada muy errónea...")
# except:
#     print("¡Buuu!")
