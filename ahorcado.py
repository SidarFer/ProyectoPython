
import random

# Función para obtener una palabra aleatoria
def obtener_palabra_aleatoria():
    palabras = ['python', 'programacion', 'desarrollo', 'computadora', 'teclado']
    return random.choice(palabras)

# Función para mostrar el tablero del ahorcado
def mostrar_tablero(intentos):
    figura = [
        '''
          +---+
          |   |
              |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
              |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
          |   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        ========''',
        '''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        ========'''
    ]
    print(figura[intentos])

# Función para jugar al ahorcado
def jugar_ahorcado():
    palabra = obtener_palabra_aleatoria()
    letras_adivinadas = []
    intentos = 0

    while True:
        mostrar_tablero(intentos)

        estado = ''
        for letra in palabra:
            if letra in letras_adivinadas:
                estado += letra + ' '
            else:
                estado += '_ '
        print(estado)

        if estado.replace(" ", "") == palabra:
            print('¡Felicidades! ¡Has adivinado la palabra correctamente!')
            break

        if intentos == 6:
            print('¡Oh no! Te has quedado sin intentos. La palabra era:', palabra)
            break

        letra = input('Ingresa una letra: ').lower()

        if len(letra) != 1 or not letra.isalpha():
            print('Por favor, ingresa una sola letra válida.')
            continue

        if letra in letras_adivinadas:
            print('Ya has ingresado esa letra antes. ¡Intenta con otra!')
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra:
            intentos += 1
            print('La letra', letra, 'no está en la palabra. ¡Te quedan', 6 - intentos, 'intentos!')

# Iniciar el juego
jugar_ahorcado()
