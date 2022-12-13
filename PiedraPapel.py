import random

numero_rondas = 0
numero_rondas = int(input('Cuantas rondas se jugaran? '))
ronda_actual = 1
opciones = ('piedra', 'papel', 'tijera')
historial_partidas = []


def transformar(seleccion):
    valor = 0
    if seleccion == 'tijera':
        valor = 0
    elif seleccion == 'papel':
        valor = 1
    elif seleccion == 'piedra':
        valor = 2
    else:
        print('Error de selección')
    return valor



def ganador(jugador, pc):
    ganador = ''
    resta = jugador - pc
    if resta == -1 or resta == 2:
        ganador = 'GANA EL JUGADOR'
    elif resta == 0:
        ganador = 'EMPATE'
    elif resta == 1 or resta == -2:
        ganador = 'GANA LA PC'
    return ganador



while numero_rondas != 0 and ronda_actual <= numero_rondas:
    print('*' * 10)
    print(f'ronda {ronda_actual}')
    print('*' * 10)
    print( )
    seleccion_jugador = input('Seleccion Jugador: piedra, papel o tijera: ')
    seleccion_pc = random.choice(opciones)
    print(f'La computadora seleccionó {seleccion_pc}')
    valor_jugador = transformar(seleccion_jugador)
    valor_pc = transformar(seleccion_pc)
    obtener_ganador = ganador(valor_jugador,valor_pc)
    print(obtener_ganador)
    print('-' * 10)
    historial_partidas.append(obtener_ganador)
    if numero_rondas == ronda_actual:
        victorias_jugador = historial_partidas.count('GANA EL JUGADOR')
        victorias_pc = historial_partidas.count('GANA LA PC')
        if victorias_jugador > victorias_pc:
            print('EL JUGADOR GANA LA SERIE')
        elif victorias_jugador < victorias_pc:
            print('LA PC OBTIENE LA VICTORIA')
        else:
            print('EMPATE DE LA SERIE')
    else: 
        pass
    ronda_actual += 1
