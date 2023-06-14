# def next_pal(numero):
#     numero += 1  # Incrementar el número en 1 para buscar el siguiente

#     while True:
#         # Convertir el número a una cadena y verificar si es un palíndromo
#         if str(numero) == str(numero)[::-1]:
#             return numero
#         else:
#             numero += 1


# numero = 11
# siguiente_palindromo = next_pal(numero)
# print(siguiente_palindromo)  # Salida: 131


def next_pal(number):

    def isPalindrome(num):
        if str(num) == str(num)[::-1]:
            return num

    next_number = number + 1

    while not isPalindrome(next_number):
        next_number = next_number + 1

    return next_number


numero = 131
siguiente_palindromo = next_pal(numero)
print(siguiente_palindromo)  # Salida: 131
