class Product:
    def __init__(self,productId,productName,description,price,quantityInStock,type):
        self.productId = productId
        self.productName = productName
        self.description = description
        self.price = price
        self.quantityInStock = quantityInStock
        self.type = type
    
    # getter
    def getProductId(self):
        return self.productId
    
    def getProductName(self):
        return self.productName
    
    def getDescription(self):
        return self.description
    
    def getPrice(self):
        return self.price
    
    def getQuantityInStock(self):
        return self.quantityInStock
    
    def getType(self):
        return self.type

    
    #setter

    def setProductId(self,productId):
        self.productId = productId

    def setProductName(self,productName):
        self.productName=productName

    def setDescription(self,description):
        self.description=description

    def setPrice(self,price):
        self.price=price

    def setQuantityInStock(self,quantityInStock):
        self.quantityInStock=quantityInStock

    def setType(self,type):
        self.type=type