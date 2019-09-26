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
	if self.tipo == 'm':
		if num == self.numero:
		    print('Numero correcto')
		    return 1

		elif num > self.numero:
		    print('El numero es menor')
		    return 0
		else:
		    print('El numero es mayor')
		    return 0
	if self.tipo == 'h':
		r = input('mayor/menor/si')
		if r == 'mayor':
			self.numero = random.randrange(self.numero, 100)
			return 0
		elif r == 'menor':
			self.numero = random.randrange(0, self.numero)
			return 0
		elif r == 'si':
			print('Numero correcto');
			return 1	


if __name__ == '__main__':
    m = 's'
    while m == 's':
        print('Comienza el juego')

        i,j = 1

        j1 = Jugador(input('Nombre jugador: '), 'h')
        maquina = Jugador('Maquina', 'm')

        maquina.piensa()
        r = 0
        while r != 1:
            print('** Turno ', i, '**')

            j1.piensa()

            r = maquina.comprueba(j1.numero)

            i += 1

        print('Enhorabuena, has acertado el número en ',i, ' intentos')
	print('Es mi turno, piensa un numero del 1 al 100')
 	r = 0
        while r != 1:
            print('** Turno ', j, '**')
	    maquina.piensa()
	    print('¿Es tu numero el ',maquina.numero,'?')

            r = j1.comprueba(maquina.numero)

            j += 1	
	
	print('He acertado en ',j,' intentos')
	if j>i:
		print('Has acertado el numero en menos intentos que yo, enhorabuena, has ganado')
	elif j == i:	
		print('Hemos acertado el numero en los mismos intentos, empate')
	else:
		print('He acertado tu numero en menos intentos que tu el mio, he vencido')


	
	
	
	
	


	
	


        m = input('¿Quieres jugar otra partida? s/n')
