import json
from urllib.request import urlopen
import csv


class ExchangeAPIClient:

    def __init__(self):
        self.rates = None

    def conecta(self):

        response = urlopen('https://api.exchangeratesapi.io/latest')
        print('Estableciendo conexión...')
        rates = json.loads(response.read())
        self.rates = rates

    def convierte(self):
        with open('/home/alumno/Escritorio/Practica 2/divisas.txt', mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            conv = 0
            f = open('/home/alumno/Escritorio/Practica 2/ahorros.txt', 'a')

            for row in csv_reader:
                conv = conv + (float(row[1]) / (self.rates['rates'][row[0]]))

            f.write(self.rates['date'] + ', ')
            f.write(str(conv) + '\n')

            print('Realizando conversion')
            print('En la fecha', self.rates['date'], 'tienes un total de',conv, 'euros')


if __name__ == '__main__':

    cliente = ExchangeAPIClient()
    cliente.conecta()
    cliente.convierte()
