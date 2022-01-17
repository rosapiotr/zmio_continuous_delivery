class Product:
    def __init__(self, id, name, price, manufacturer):
        self.id = id
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        
    def to_json(self):
        return {"id": self.id, "name": self.name, "price": self.price, "manufacturer": self.manufacturer}

    @classmethod
    def from_json(self, data):
        return self(**data)
