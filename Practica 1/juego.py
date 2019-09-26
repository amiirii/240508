import random

class Jugador:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def piensa(self):
        if self.tipo == 'm':
            self.numero = random.randrange(0, 100)
        else:
            self.numero = input('{}, ¿cuál es tu número?\n'.format(self.nombre))

    def piensam(self,num,ant):
        r = input('mayor/menor/si\n')
        if r == 'menor':
            self.numero = random.randrange(ant, num)
            return 0
        elif r == 'mayor':
            self.numero = random.randrange(num, ant)
            return 0
        elif r == 'si':
            print('Numero correcto')
            return 1

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
        print('He pensado un numero del 0 al 100, intenta acertarlo')

        i = 1
        j = 1

        j1 = Jugador(input('Nombre jugador: \n'), 'h')
        maquina = Jugador('Maquina', 'm')

        maquina.piensa()
        r = 0
        while r != 1:
            print('** Turno ', i, '**')

            j1.piensa()
            r = maquina.comprueba(int(j1.numero))

            i += 1

        print('Enhorabuena, has acertado el número en ', i - 1, ' intentos')
        print('Es mi turno, piensa un numero del 1 al 100')

        maquina.piensa()
        min = 0
        max = 100
        r = 0

        while r != 1:
            print('** Turno ', j, '**')
            print('¿Es tu numero el',maquina.numero,'?')

            r = input('mayor/menor/si\n')
            if r == 'menor':
                max = maquina.numero
                if max == maquina.numero:
                    max = maquina.numero - 1
                maquina.numero = random.randrange(min, maquina.numero)
                r = 0
            elif r == 'mayor':
                min = maquina.numero
                if min == maquina.numero:
                    min = maquina.numero + 1
                maquina.numero = random.randrange(maquina.numero, max)
                r = 0
            elif r == 'si':
                print('Numero correcto')
                r = 1

            j += 1

        print('He acertado en ', j - 1, ' intentos')
        if j > i:
            print('Has acertado el numero en menos intentos que yo, enhorabuena, has ganado')
            m = input('¿Quieres jugar de nuevo? s/n\n')
        elif j == i:
            print('Hemos acertado el numero en los mismos intentos, empate')
            m = input('¿Quieres jugar de nuevo? s/n\n')
        else:
            print('He acertado tu numero en menos intentos que tu el mio, he vencido')
            m = input('¿Quieres jugar de nuevo? s/n\n')
