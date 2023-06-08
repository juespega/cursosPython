"""
Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.
"""
blocks = int(input("Ingresa el número de bloques: "))

height = 0
nivel = 1
while nivel <= blocks:
    blocks -= nivel
    nivel += 1
    height += 1

print("La altura de la pirámide:", height)


"""
bloques = int(input("Ingrese el número de bloques:"))
 
 
cotaSuperior = 0 #Cada piso (altura) de la pirámide, tiene un número máximo de bloques que se pueden utilizar
altura = 0
altura2: 0
 
while True:
 
#Aplico la condición para que mi contador vaya avanzado hasta alcanzar un máximo de bloques a una altura.
 
      if bloques <= cotaSuperior:
 
            # Si el límite superior menos los bloques ingresados es igual a cero ( no sobran ni faltan bloques), imprime el contador altura, hasta donde haya avanzado.
         if (cotaSuperior - bloques) == 0:
 
          print("La altura de la pirámide:", altura)
          break
 
            # Si el límite superior menos los bloques ingresados es mayor a cero (faltan bloques para completar el nivel), imprime el contador altura aterior (altura2).
         if (cotaSuperior - bloques) > 0:
 
          print("La altura de la pirámide:", altura2)
          break
 
      else:
 
        altura = altura + 1
        altura2 = altura - 1
 
      # Este es el contador que viene asociado con los bloques utilizados por cada altura alcanzada.
        cotaSuperior = cotaSuperior + altura
"""
