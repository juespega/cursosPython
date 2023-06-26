"""
Ahora trabajaremos con triángulos. 
Comenzaremos con una función que verifique si tres lados de ciertas
longitudes pueden formar un triángulo.

En la escuela aprendimos que la suma arbitraria de dos lados tiene que ser mayor
que la longitud del tercer lado.

No será algo difícil. La función tendrá tres parámetros - uno para cada lado.

Regresará True si todos los lados pueden formar un triángulo,
y False de lo contrario. En este caso, is_a_triangle es un buen nombre para dicha función.
"""


# def is_a_triangle(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))


# def is_a_triangle(a, b, c):
#     if a + b <= c or b + c <= a or c + a <= b:
#         return False
#     return True


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# print(is_a_triangle(1, 1, 1))
# print(is_a_triangle(1, 1, 3))


# def is_a_triangle(a, b, c):
#     return a + b > c and b + c > a and c + a > b


# a = float(input('Ingresa la longitud del primer lado: '))
# b = float(input('Ingresa la longitud del segundo lado: '))
# c = float(input('Ingresa la longitud del tercer lado: '))

# if is_a_triangle(a, b, c):
#     print('Si, si puede ser un triángulo.')
# else:
#     print('No, no puede ser un triángulo.')


"""
En el segundo paso, intentaremos verificar si un triángulo es un triángulo rectángulo.

Para ello haremos uso del Teorema de Pitágoras:

c2 = a2 + b2

¿Cómo saber cual de los tres lados es la hipotenusa?

La hipotenusa es el lado más largo.
"""

def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))