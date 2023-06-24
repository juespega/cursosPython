"""
Definamos una función que calcula el Índice de Masa Corporal (IMC).

Como puedes observar, la formula ocupa dos valores:

peso (originalmente en kilogramos)
altura (originalmente en metros)
La nueva función tendrá dos parámetros. Su nombre será bmi,
pero si prefieres utilizar otro nombre, adelante.
"""

# def bmi(weight, height):
#     return weight / height ** 2


# print(bmi(81, 1.82))


# # Calcular el IMC y convertir unidades del Sistema Inglés al Sistema Métrico

# def bmi(weight, height):
#     #El símbolo de diagonal invertida (\) es empleado. Si se termina una línea de código con el,
#     #Python entenderá que la línea continua en la siguiente
#     if height < 1.0 or height > 2.5 or \
#         weight < 20 or weight > 200:
#         return None

#     return weight / height ** 2


# print(bmi(81, 2.82))


# def lb_to_kg(lb):
#     return lb * 0.45359237


# print(lb_to_kg(1))


# def ft_and_inch_to_m(ft, inch):
#     return ft * 0.3048 + inch * 0.0254

# print(ft_and_inch_to_m(1, 1))
# # Vamos a convertir seis pies a metros:
# print(ft_and_inch_to_m(6, 0))


# def ft_and_inch_to_m(ft, inch = 0.0):
#     return ft * 0.3048 + inch * 0.0254


# print(ft_and_inch_to_m(6))


def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


def lb_to_kg(lb):
    return lb * 0.4535923


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None

    return weight / height ** 2


print(bmi(weight=lb_to_kg(176), height=ft_and_inch_to_m(5, 7)))
