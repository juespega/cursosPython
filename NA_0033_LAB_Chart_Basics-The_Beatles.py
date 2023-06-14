"""
Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

Por cierto, ¿eres fan de los Beatles? (Los Beatles son una de las bandas favoritas de Greg. 
Pero espera...¿Quién es Greg?)
"""
# paso 1: crea una lista vacía llamada beatles;
beatles = []
print("Lista vacia: ", beatles)

#paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: 
#John Lennon, Paul McCartney y George Harrison;
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Lista con los Beatles: ", beatles)

# paso 3: emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros
#de la banda a la lista: Stu Sutcliffe, y Pete Best;
new_member = ""
for member in beatles:
    new_member = (input("Ingresa los miembros faltantes de a uno: "))
    if new_member == "0": 
        break
    else:
        beatles.append(new_member)
    

print("Lista con los Beatles: ", beatles)

#paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
del beatles[3]
del beatles[4]

print("Lista con los Beatles: ", beatles)

# paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.
beatles.insert(0, "Ringo Starr")
print("Lista con los Beatles: ", beatles)