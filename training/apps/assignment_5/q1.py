from math import pi
from abc import abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        raise NotImplementedError("Area needs to be implemented.")

    @classmethod
    def get(cls, name: str):

        """
        Method to get sub-class object by name of shape
        """

        for shape in cls.__subclasses__():
            if shape.__name__ == name:
                return shape

        return None

class Square(Shape):

    def __init__(self, side: float) -> None:
        super().__init__()
        self.side = side

    def area(self):
        return self.side**2

class Triangle(Shape):

    def __init__(self, base: float, height: float) -> None:
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return (self.base*self.height)/2.0

class Circle(Shape):

    def __init__(self, radius: float) -> None:
        super().__init__()
        self.radius = radius

    def area(self):
        return 2.0*pi*self.radius
