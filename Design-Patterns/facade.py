class GerenciamentoEventos:

    def __init__(self):
        print('GerenciamentoEventos :: Vou organizar com todo mundo! \n\n')

    def organizar(self):
        self.salao = SalaoFestas()
        self.salao.agendar()

        self.florista = Florista()
        self.florista.arranjar_flores()

        self.comida = Restaurante()
        self.comida.preparar()

        self.musica = Banda()
        self.musica.montar_palco()
    

class SalaoFestas:

    def __init__(self):
        print('SalaoFestas :: Agendando o salao de festas')

    def esta_disponivel(self):
        print('SalaoFestas :: Este salão de festas está disponível?')
        return True

    def agendar(self):
        if self.esta_disponivel():
            print('SalaoFestas :: Agendamento do salao realizado \n')


class Florista:

    def __init__(self):
        print('Florista :: Flores para um evento?')

    def arranjar_flores(self):
        print('Florista :: Rosas, Margaridas e Lírios serão usados ...\n')


class Restaurante:

    def __init__(self):
        print('Restaurante :: Comida para eventos?')

    def preparar(self):
        print('Restaurante :: Comida chinesa e brasileira serão servidas...\n')

    
class Banda:

    def __init__(self):
        print('Banda :: Arranjos musicais para eventos')

    def montar_palco(self):
        print('Banda :: Preparando o palco para tocar jazz e rock em eventos')

    
class Cliente:

    def __init__(self):
        print('Cliente :: Uau! Preparação para o casamento')

    def contrata_gerente_eventos(self):
        print('Cliente :: Vou contratar uma empresa para gerenciar eventos \n')

        ge = GerenciamentoEventos()
        ge.organizar()

    def __del__(self):
        print('Cliente :: Foi muito simples organizar este evento com o Facade')


if __name__ == '__main__':
    cliente = Cliente()
    cliente.contrata_gerente_eventos()