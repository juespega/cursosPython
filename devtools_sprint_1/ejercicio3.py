"""
Se define la función countNameRepetitions que toma como parámetro names, 
que es el array de nombres.
"""
def countNameRepetitions(names):

    """
    Se crea un diccionario vacío 'count' que se utilizará 
    para contar cuántas veces se repite cada nombre.
    """
    count = {}

    """
    Se itera sobre cada nombre en el array names. 
    Para cada nombre, se verifica si ya existe como una clave en el diccionario count. 
    Si es así, se incrementa el contador correspondiente al nombre en 1. 
    Si no existe como clave, se agrega la clave al diccionario count 
    y se establece su valor inicial en 1.
    """
    for name in names:
        if name in count:
            count[name] += 1
        else:
            count[name] = 1

    """
    Se crea un diccionario vacío result que se utilizará para 
    almacenar el nombre y su representación de asteriscos correspondiente.
    """
    result = {}

    """
    Se itera sobre cada par clave-valor en el diccionario name_count. 
    Para cada par, se asigna al diccionario result la clave name 
    y se le asigna un string de asteriscos * multiplicado por el valor count correspondiente.
    """
    for name, count in count.items():
        result[name] = '*' * count

    return result


names2 = ['Juan', 'María', 'Pedro', 'Juan', 'María', 'María']
result2 = countNameRepetitions(names2)
print(result2)
