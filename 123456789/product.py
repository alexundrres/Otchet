class Product:
    def __init__(self, product_id, name, price, availability, weight):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.availability = availability
        self.weight = weight

    def __str__(self):
        return f"ID товара: {self.product_id}, Название: {self.name}, Цена: {self.price}, Наличие: {self.availability}, Вес: {self.weight}"

