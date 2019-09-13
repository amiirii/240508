import random


class Jugador:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def piensa(self):
        if self.tipo == 'm':
            self.numero = random.randrange(0, 100)
        else:
            self.numero = input('{}, ¿cuál es tu número?'.format(self.nombre))

    def comprueba(self, num):
        if num == self.numero:
            print('Numero correcto')
            return 1

        elif num > self.numero:
            print('El numero es menor')
            return 0
        else:
            print('El numero es mayor')
            return 0


if __name__ == '__main__':
    m = 's'
    while m == 's':
        print('Comienza el juego')

        i = 1

        j1 = Jugador(input('Nombre jugador: '), 'h')
        maquina = Jugador('Maquina', 'm')

        maquina.piensa()
        r = 0
        while r != 1:
            print('** Turno ', i, '**')

            j1.piensa()

            r = maquina.comprueba(j1.numero)

            i += 1

        print('Enhorabuena, has acertado el número')
        m = input('¿Quieres jugar otra partida? s/n')






