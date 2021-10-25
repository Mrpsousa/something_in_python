class Motor:

    def ligar(self):
        print('Motor Ligado...')
     

class Pneu:

    def enxer(self):
        print('Pneu cheio...')

class Carro:

    def __init__(self, modelo):
        self.modelo = modelo
        self.motor = Motor()
        self.pneu = Pneu()

carro = Carro('Fusca')
carro.motor.ligar()
print(carro.modelo)