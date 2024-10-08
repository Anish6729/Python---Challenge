from Product import Product

class Clothing(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, size, color):
        super().__init__(productId, productName, description, price, quantityInStock, "Clothing")
        self.size = size
        self.color = color