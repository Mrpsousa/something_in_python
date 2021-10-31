from abc import ABCMeta, abstractmethod


class Secao(metaclss=ABCMeta):

    @abstractmethod
    def __repr__(self):
        pass


class SecaoPessoal(Secao):

    def __repr__(self):
        return 'Seção Pessoal'


class SecaoAlbum(Secao):

    def __repr__(self):
        return 'Seção Álbum'


class SecaoProjeto(Secao):

    def __repr__(self):
        return 'Seção Projeto'


class SecaoPublicacao(Secao):

    def __repr__(self):
        return 'Seção Publicacao'


class Perfil(metaclass=ABCMeta):

    def __init__(self):
        self.secoes = []
        self.criar_perfil()

    @abstractmethod
    def criar_perfil(self):
        pass

    def get_secoes(self):
        return self.secoes

    def add_secao(self, secao):
        self.secoes.append(secao)