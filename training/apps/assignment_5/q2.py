from abc import abstractmethod

class Car:

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str
    ) -> None:
        
        self.speed = speed
        self.regular_price = regular_price
        self.color = color

    def doublegetSalePrice(self):
        
        return self.regular_price

class Truck(Car):

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str, 
        weight: float
    ) -> None:
        
        super().__init__(speed, regular_price, color)
        
        self.weight = weight

    def doublegetSalePrice(self):
        
        if self.weight > 2000.0:
            return self.regular_price*0.9
        
        return self.regular_price

class Ford(Car):

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str, 
        manufacturer_discount: 
        float
    ) -> None:
        
        super().__init__(speed, regular_price, color)

        self.manufacturer_discount = manufacturer_discount

    def doublegetSalePrice(self):
    
        return self.regular_price - self.manufacturer_discount

class Sedan(Car):

    def __init__(
        self, 
        speed: int, 
        regular_price: float, 
        color: str, 
        length: float
    ) -> None:
    
        super().__init__(speed, regular_price, color)
        self.length = length

    def doublegetSalePrice(self):
        
        if self.length > 20.0:
            return self.regular_price*0.95

        return self.regular_price*0.90