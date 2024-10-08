from Model.Product import Product
from Model.User import User
from DAO.IOrderManagementRepository import IOrderManagementRepository
from Util.DBUtil import DBUtil
from Exception.UserNotFound import UserNotFound
from Exception.OrderNotFound import OrderNotFound

class OrderProcessor(IOrderManagementRepository):
    
    def __init__(self):
        self.conn = DBUtil.getDBConn()


    def validateUser(self, username):
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT role FROM Users WHERE username = ?", (username))
        user_role = cursor.fetchone()
        
        if user_role is None:
            return False, "\nUser Not Found !!\n\n"
        
        if user_role[0].lower() != "admin":
            return False, "\nPermission Denied!, Only admins can create products\n\n"
    
        return True, "\nUser is an admin. Proceed with product creation.\n\n"
    
    def createUser(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO Users (userid, username, password, role) VALUES (?, ?, ?, ?)",
                        (user.userId ,user.username, user.password, user.role))
            self.conn.commit()
            return True
        except Exception as error:
            print("\ERROR  : ", error)
            return False
        finally:
            cursor.close()

    # def createProduct(self, user, product):   
    def createProduct(self, user, product):
        try:
            cursor = self.conn.cursor()
            if user.role.lower()=='admin':
                cursor.execute("INSERT INTO Products (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)",
                            (product.productId, product.productName, product.description, product.price, product.quantityInStock, product.type))
                
                # cursor.execute("INSERT INTO ELECTRONICS (productId, brand, warrantyPeriod) VALUES (?, ?, ?)",
                #                product.productId, product.brand, product. warrantyPeriod)
                self.conn.commit()
                return True
            else:
                print("\nPermission Denied!, Only admins can create products\n\n")
                return False
        except Exception as error:
            print("\nERROR:  ", error)
            return False
        finally:
            cursor.close()

    def createOrder(self, user, productList):      #user, productList
        try: 
            cursor = self.conn.cursor()
            
            # Checking if the user already exists in the Users table
            cursor.execute("SELECT userId FROM Users WHERE userId = ?", (user.userId))
            result = cursor.fetchone()

            if not result:      # creating new user 
                cursor.execute("INSERT INTO Users (userid, username, password, role) VALUES (?, ?, ?, ?)",
                        (user.userId ,user.username, user.password, user.role))

            for product in productList:
                # Check if the product is available in stock
                cursor.execute("SELECT quantityInStock FROM Products WHERE productId = ?", (product.productId))
                currQuantity = cursor.fetchone()

                ordererdProductQuantity = product.quantityInStock
                
                if currQuantity and currQuantity[0] >= ordererdProductQuantity:
                    # Insert the order into Orders table with orderId, userId, productId, and quantity
                    cursor.execute("INSERT INTO Orders (userId, productId, quantity) VALUES (?, ?, ?)",
                                (user.userId, product.productId, product.quantityInStock))
                    
                    # Updating the product stock 
                    cursor.execute("UPDATE Products SET quantityInStock = quantityInStock - ? WHERE productId = ?",
                                (ordererdProductQuantity, product.productId))
                    print("\nOrdered has been created !\n\n")
                else:
                    print(f"\nProduct with ID {product.productId} is out of stock !\n\n") 
                
            self.conn.commit()

        except Exception as error:
            print("\ERROR  : ", error)
        finally:
            cursor.close()
        

    def cancelOrder(self, userId, orderId):
        try:   
            cursor = self.conn.cursor() 
            cursor.execute("SELECT * FROM Users WHERE userId = ?", (userId,))
            user = cursor.fetchone()
            if not user:
                raise UserNotFound(f"User with ID {userId} not found !\n")

            # Checking if the order exists
            cursor.execute("SELECT * FROM Orders WHERE userId = ? AND orderId = ?", (userId, orderId))
            order = cursor.fetchone()
            if not order:
                raise OrderNotFound(f"Order with ID {orderId} not found for User {userId} !\n")

            # Cancelling the order
            cursor.execute("Delete from orders where orderid = ?", (orderId))
            print("\nOrder has been cancelled\n")
            
            self.conn.commit()
        except UserNotFound as error:
            print("Error:", error)
        except OrderNotFound as error:
            print("Error:", error)
        except Exception as error:
            print("ERROR:", error)
        finally:
            cursor.close()

    def getAllProducts(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Products")
        data= cursor.fetchall()
        return data

    def getOrderByUser(self, user):
        try:
            cursor = self.conn.cursor()
            cursor.execute(""" SELECT 
                                o.orderId, p.productName, p.description, p.price, o.userId, o.productId 
                        FROM Orders o 
                        JOIN Users u ON o.userId = u.userId 
                        JOIN Products p ON o.productId = p.productId 
                        WHERE u.userId = ?""", (user.userId))
            data= cursor.fetchall()
            return data
        except UserNotFound as error:
            print("Error:", error)
        except Exception as error:
            print("Error:", error)
        finally:
            cursor.close()
    

# obj=OrderProcessor()
# obj.createOrder(2,20)
# print(obj.createOrder(1, "laptop"))
# print(obj.validateUser("dan"))
# print(obj.getOrderByUser("anish"))
