print('Este programa compara dos numeros ingresados por el usuario')
num_1 = int(input('Escribe un nuemero'))
num_2 = int(input('Escribe el otro numero a comparar'))
 
if num_1 == num_2:
    print(str(num_1) + ' Es igual que ' + str(num_2))
elif num_1 > num_2:
    print( str(num_1) +' Es mayor que '+ str(num_2))
else:
    print(str(num_1) +' Es menor que '+ str(num_2))
