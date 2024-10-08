import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Model.Product import Product

from DAO.OrderProcessor import OrderProcessor
from Model.User import User
from Model.Product import Product


class OrderManagement:

    def main():
        orderProcessor = OrderProcessor()
        while True:
            print("\n---------Order Management System Menu ----------------\n")
            print("Choose an option: ")
            print("1. Create User")
            print("2. Create Product")
            print("3. Create Order")
            print("4. Cancel Order")
            print("5. Get All Products")
            print("6. Get Orders by User")
            print("7. Exit")

            choice = int(input("\nEnter choice: "))

            if choice == 1:                         # Create User
                # userId, username, password, role
                userId= int(input("Enter user Id: "))
                userName = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")
                user = User(userId, userName, password, role)
                response = orderProcessor.createUser(user)
                if response:
                    print("\nUser created successfully!\n\n")
                else:
                    print("Something got wrong :(\n)")
            
            elif choice == 2:                       # Create Product
                # productId, productName, description, price, quantityInStock, type
                userId= int(input("Enter user Id: "))
                userName = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")
                user = User(userId, userName, password, role)

                print("\n")
                # (isValid, message) =orderProcessor.validateUser(userName)

                # if(isValid):
                productId= int(input("Enter Product ID: "))
                productName= input("Enter Product Name: ")
                description= input("Enter Product Description: ")
                price= int(input("Enter Price: "))
                quantityInStock= int(input("Enter the quantity in Stock: "))
                type=input("Enter type (Electronic/Clothing): ")

                # if(type.lower()=="electronic"):
                #     brand=input("Enter brand: ")    
                #     warrantyPeriod=int(input("Enter Warranty Period: "))

                #     product=Electronics(productId, productName, description, price, quantityInStock, brand, warrantyPeriod)
                # elif(type.lower()=="clothing"):
                #     color=input("Enter color: ")
                #     size=int(input("Enter size: "))
                #     product=Clothing(productId, productName, description, price, quantityInStock, size, color)
                # else:
                #     print("Invalid Produt Type !!\n")
                product= Product(productId,productName,description,price,quantityInStock,type)

                response = orderProcessor.createProduct(user,product)
                if response:
                    print("\nProduct created Successfully !!\n\n")
                else:
                    print("\n Product creation Fail !\n\n")
                # else:
                #     print(message)

            elif choice == 3:                       # Create Order
                userId=int(input("Enter Your User Id: "))
                userName = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (Admin/User): ")

                user = User(userId, userName, password, role)   # check if user exists , if not, then create user with this details

                productList=[]
                while True:
                    productId = int(input("Enter product ID (Enter 0 to finish): "))
                    if productId == 0:
                        break

                    productQuantity = int(input("Enter product quantity: "))
                    product = Product(productId, "", "", 0, productQuantity, "")
                    productList.append(product)

                orderProcessor.createOrder(user, productList)  
                print("Thank you for ordering !\n")

            elif choice == 4:                       # Cancel Order Logic
                userId=int(input("Enter User Id: "))
                orderId=int(input("Enter Order Id you want to cancel: "))
                orderProcessor.cancelOrder(userId,orderId)
            
            elif choice == 5:                       # Get all products
                products = orderProcessor.getAllProducts()
                for product in products:
                    print(product)
                print("\n")
            
            elif choice == 6:                       # Get Orders by User
                userId= input("Enter User Id : ")
                user= User(userId,"","","")
                orders=orderProcessor.getOrderByUser(user)
                # print("orderId, productName, description, price, userId, productId\n")
                for order in orders:
                    print(order)
                print("\n")

            elif choice == 7:                       # Exit
                break

            else:
                print("Invalid choice !")


if __name__ == "__main__":
    OrderManagement.main()
