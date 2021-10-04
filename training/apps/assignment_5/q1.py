from math import pi
from abc import abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        raise NotImplementedError("area() needs to be implemented.")

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

    def __init__(self, kwargs) -> None:
        super().__init__()
        self.side = float(kwargs['side'])

    def area(self):
        return self.side**2

    def get_args():
        return ['side']

class Triangle(Shape):

    def __init__(self, kwargs) -> None:
        super().__init__()
        self.base = float(kwargs['base'])
        self.height = float(kwargs['height'])

    def area(self):
        return (self.base*self.height)/2.0

    def get_args():
        return ['base','height']

class Circle(Shape):

    def __init__(self, kwargs) -> None:
        super().__init__()
        self.radius = float(kwargs['radius'])

    def area(self):
        return 2.0*pi*self.radius

    def get_args():
        return ['radius']