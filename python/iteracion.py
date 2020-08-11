dia = 1
hora = 1
minuto = 1
segundo = 1
while dia < 8:
    while hora < 24:
        while minuto < 60:
            while segundo < 60:
                print(dia, hora, minuto, segundo)
                segundo += 1
            minuto += 1
            segundo = 0
        hora += 1
        minuto = 0
    dia += 1
    hora = 0
print('Ha pasado una semana')


    