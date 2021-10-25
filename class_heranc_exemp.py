class Pessoa:
    def __init__(self, name):
        self.__name = name

    def andar(self):
        print(f'{self.__name} está andando')

class Aluno(Pessoa):
    def __init__(self, name, matricula):
        super().__init__(name)
        self.__matricula = matricula

aluno = Aluno('Maria', 1234)
aluno.andar()