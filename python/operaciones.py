def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
        return resultados
nums = [2, 2, 3]
print(multiplicar_por_dos(nums))
# funciones en expresiones 
sumar = lambda x, y: x + y
print(sumar(2, 3))