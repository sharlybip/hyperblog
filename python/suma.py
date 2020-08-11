def suma(a, b):
    total = a + b
    return total
print(suma(2, 4)) 

def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'
print(nombre_completo('Carlos', 'Dominguez',inverso=True))
print(nombre_completo('Carlos', 'Dominguez'))
print(nombre_completo(apellido= 'dominguez', nombre='Carlos'))