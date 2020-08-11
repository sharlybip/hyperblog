print('...............Comparador de edades...........\n .....Primer humano......\n')
nombre_1 = input('Escribe tu nombre: ')
nombre_1_edad = int(input('Escribe tu edad: '))
nombre_2 = input('Escribe tu nombre: ')
nombre_2_edad = int(input('Escribe tu edad: '))
if nombre_1_edad < nombre_2_edad :
    print(nombre_1 + ', es menor que ' + nombre_2)
elif nombre_1_edad > nombre_2_edad :
    print(nombre_1 + ', es mayor que ' + nombre_2)
else:
    print(nombre_1 + 'y' + nombre_2 + ', son de la misma edad')
