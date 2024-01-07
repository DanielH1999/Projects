import random

def user_guess(chances):

    max = int(input('adivinar el numero entre 1 y ... ')) #pedir un numero maximo

    num = random.randint(1, max) #decidir numero

    e = 0 #inicializamos variable que vamos a usar para eleccion del jugador

    while e != num and chances > 0:

        print(f'tenes {chances} turnos\n')

        e = int(input(f'dame un numero entre 1 y {max}: ')) #pedir un numero del usuario

        if e < 1 or e > max: #si (n < 1 o n > max)
            print(f'saliste del juego ')
            return
        elif e > num:
            print('tu numero es muy grande')
        elif e < num:
            print('tu numero es muy chico')

        chances -= 1
        
    if chances > 0:
        print('ganaste!')
    else:
        print('perdiste!')
    print(f'{num} era el correcto!')


def computer_guess(max):
    bajo = 1 #el numero mas bajo posible
    alto = max #el numero mas alto posible
    respuesta = '' #donde vamos a almacenar la respuesta del usuario

    while respuesta != 'c': #c de correcto
        num = random.randint(bajo, alto)
        respuesta = input(f"tu numero es {num}? (correcto: 'c', muy alto: 'a', muy bajo 'b', salir: 's'):\n")
        if respuesta == 's':
            print("saliste del juego 's'")
            return
        elif respuesta == 'a':
            alto = num - 1
        elif respuesta == 'b':
            bajo = num + 1
    
    print(f'tu numero era {num}!')

game_mode = int(input('selecciona el modo de juego:\n\
    1- adivinar el numero elegido al azar por la computadora\n\
    2- pensar en un numero y que la computadora lo adivine\n'))

if game_mode == 1:
    user_guess(10)
elif game_mode == 2:
    computer_guess(1000)
else:
    print('seleccion invalida')