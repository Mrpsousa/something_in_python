from abc import ABCMeta, abstractmethod


#AbstractFactory
class PizzaFactory(metaclass=ABCMeta):

    @abstractmethod
    def criar_pizza_veg(self):
        pass

    @abstractmethod
    def criar_pizza(self):
        pass

#ConcretFactoryA
class PizzaBrasileira(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaMandioca()

    def criar_pizza(self):
        return PizzaMandioca()


#ConcretFactoryB
class PizzaItaliana(PizzaFactory):

    def criar_pizza_veg(self):
        return PizzaBrocoli()

    def criar_pizza(self):
        return PizzaBolonha()


# AbstractProductA
def PizzaVeg(metaclass=ABCMeta):

    @abstractmethod
    def preparar(self, PizzaVeg):
        pass


# AbstractProductB
def Pizza(metaclass=ABCMeta):

    @abstractmethod
    def servir(self, PizzaVeg):
        pass


# ProductConcret
def PizzaMandioca(PizzaVeg):

    def preparar(self):
        print(f'Preparando {type(self).__name__}')


# ProductConcret
def PizzaCamarao(Pizza):

    def servir(self, PizzaVeg):
        print(f'{type(self).__name__} é servida com camarão {type(PizzaVeg).__name}')