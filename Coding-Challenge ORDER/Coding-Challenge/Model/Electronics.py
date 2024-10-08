from Product import Product

class Electronics(Product):
    def __init__(self, productId, productName, description, price, quantityInStock, brand, warrantyPeriod):
        super().__init__(productId, productName, description, price, quantityInStock, "Electronics")
        self.brand = brand
        self.warrantyPeriod = warrantyPeriod


# obj= Electronics(1,"anish","hello",20,2,"samsung",2)
# print(type(obj).__class_name__)

    
    
