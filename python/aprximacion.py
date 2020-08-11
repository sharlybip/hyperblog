objetivo = int(input('Escoge un numero'))
epsilon = 0.0001
paso = epsilon**2
respuesta = 0.0
print(paso)
while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso
if abs(respuesta**2 -objetivo) >= epsilon:
    print(f'No se encuentra la raiz cuadrada {objetivo}')
else:
    print(type(respuesta))
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')