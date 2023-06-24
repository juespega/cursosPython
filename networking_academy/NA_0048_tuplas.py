# # TUPLAS

# # ¿Cómo crear una tupla?
# emty_tuple = ()
# tuple_1 = (1, 2, 4, 8)
# tuple_2 = 1., .5, .25, .125

# print(tuple_1, tuple_2)

# one_element_tuple_1 = (1, )
# one_element_tuple_2 = 1.,

# print(one_element_tuple_1, one_element_tuple_2)


# # ¿Cómo utilizar un tupla?
# # Leer los elementos

# my_tuple = (1, 10, 100, 1000)

# print(my_tuple[0])
# print(my_tuple[-1])
# print(my_tuple[1:])
# print(my_tuple[:-2])

# for elem in my_tuple:
#     print(elem)


# my_tuple = (1, 10, 100)

# t1 = my_tuple + (1000, 10000)
# t2 = my_tuple * 3

# print(len(t2))
# print(t1)
# print(t2)
# print(10 in my_tuple)
# print(-10 not in my_tuple)

# var = 123

# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)

# t1, t2, t3 = t2, t3, t1

# print(t1, t2, t3)


# # Completa el código para emplear correctamente el método count()
# # para encontrar la cantidad de 2 duplicados en la tupla siguiente.

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicates = tup.count(2)

# print(duplicates)    # salida: 4


#  Escribe un programa que convierta la lista my_list en una tupla.
# my_list = ["car", "Ford", "flower", "Tulip"]

# t = tuple(my_list)
# print(t)
