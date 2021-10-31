from abc import ABC, abstractmethod, ABCMeta


class FormasInterface(metaclass=ABCMeta):

    @abstractmethod
    def get_perimetro(self) -> int:
        pass

    @abstractmethod
    def get_area(self) -> int:
        pass