"""Operadores abreviados"""

i = 1
j = 2
var = 3
rem = 4
x = 5


# Expresiones
i = i + 2 * j
var = var / 2
rem = rem % 10
j = j - (i + var + rem)
x = x ** 2
print(i, var, rem, j, x, sep=",")

# Operador Abreviado
i += 2 * j
var /= 2
rem %= 10
j -= (i + var + rem)
x **= 2
print(i, var, rem, j, x, sep=",")
