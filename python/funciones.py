objetivo = int(input('Escoge un numero: '))
busqueda = int(input('si quiere buscar la raiz con buqueda binaria precione 1, si quieres hacerlo por busqueda binaria presiona 2: '))


def aproximacion(epsilon): 
    
    paso = epsilon**2
    respuesta = 0.0
    print(paso)
    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        print(abs(respuesta**2 - objetivo), respuesta)
        respuesta += paso
    if abs(respuesta**2 -objetivo) >= epsilon:
        print(f'No se encuentra la raiz cuadrada {objetivo}')
        
    else:
        return f'La raiz cuadrada de {objetivo} es {respuesta}'
def binary(epsilon):
    
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto +bajo) / 2 

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        respuesta = (alto + bajo) / 2
    return f'La raiz cuadrada de {objetivo} es {respuesta}'
while objetivo != 1 and objetivo != 2:
    if busqueda == 1:
        print(aproximacion(0.0001))
        break
    elif busqueda == 2:
        print(binary(0.0001))
        break
    else:
        print('solo puede escoger uno o dos')
        break