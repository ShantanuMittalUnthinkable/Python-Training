from abc import abstractmethod, abstractclassmethod

class Car:

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str
    ) -> None:
        
        self.speed = int(speed)
        self.regular_price = float(regular_price)
        self.color = color

    def doublegetSalePrice(self):
        
        return self.regular_price

    @classmethod
    def get(cls, name: str):

        """
        Method to get sub-class object by name of shape
        """

        for shape in cls.__subclasses__():
            if shape.__name__ == name:
                return shape

        return None

    @classmethod
    def get_extra_args(cls):

        raise NotImplementedError("get_extra_args() is required to be implemented.")

class Truck(Car):

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str, 
        kwargs
    ) -> None:
        
        super().__init__(speed, regular_price, color)
        
        self.weight = float(kwargs['weight'])

    def doublegetSalePrice(self):

        if self.weight > 2000.0:
            return self.regular_price*0.90
        
        return self.regular_price

    @classmethod
    def get_extra_args(cls):

        return ['weight']

class Ford(Car):

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str, 
        kwargs
    ) -> None:
        
        super().__init__(speed, regular_price, color)

        self.manufacturer_discount = float(kwargs['manufacturer_discount'])

    def doublegetSalePrice(self):
    
        return self.regular_price - self.manufacturer_discount

    @classmethod
    def get_extra_args(cls):

        return ['manufacturer_discount']

class Sedan(Car):

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str, 
        kwargs
    ) -> None:
    
        super().__init__(speed, regular_price, color)
        self.length = float(kwargs['length'])

    def doublegetSalePrice(self):
        
        if self.length > 20.0:
            return self.regular_price*0.95

        return self.regular_price*0.90

    @classmethod
    def get_extra_args(cls):

        return ['length']