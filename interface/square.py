from forms import FormasInterface

class Square(FormasInterface):

    def __init__(self, side: int) -> None:
        self.side = side

    def get_perimetro(self) -> int:
        perimetro = self.side * 4
        return perimetro

    def get_area(self) -> int:
        area = self.side * self.side
        return area


obj = Square(5)