create database Order_Management_System;
use Order_Management_System;


CREATE TABLE Users (
    --userId INT PRIMARY KEY IDENTITY(1,1),
    userId INT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    role VARCHAR(20)
);

drop table Users;
drop table Products;
/*
SELECT CONSTRAINT_NAME
FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
WHERE TABLE_NAME = 'Users' AND CONSTRAINT_TYPE = 'PRIMARY KEY';

ALTER TABLE Users
DROP CONSTRAINT PK__Users__CB9A1CFF739AA669;

ALTER TABLE Users
ADD CONSTRAINT userId INT PRIMARY KEY IDENTITY(1,1);*/


CREATE TABLE Products (
    productId INT PRIMARY KEY,
    productName VARCHAR(100),
    description VARCHAR(255),
    price DECIMAL(10, 2),
    quantityInStock INT,
    type VARCHAR(50)
);

--SELECT quantityInStock FROM Products WHERE productId = 10;

CREATE TABLE Orders (
    orderId INT PRIMARY KEY IDENTITY(1,1),
    userId INT FOREIGN KEY REFERENCES Users(userId),
    productId INT FOREIGN KEY REFERENCES Products(productId)
);

alter table Orders add quantity int;

CREATE TABLE Electronics (
    productId INT primary key, 
	brand varchar(50),
	warrantyPeriod int,
	FOREIGN KEY (productId) REFERENCES Products(productId)
);

CREATE TABLE Clothing (
    productId INT primary key, 
	size int,
	color varchar(20),
	FOREIGN KEY (productId) REFERENCES Products(productId)
);

select * from Orders;
select * from Products;
select * from Users;


SELECT 
    o.orderId, 
    p.productName, 
    p.description, 
    p.price, 
    o.userId, 
    o.productId
FROM Orders o
JOIN Users u ON o.userId = u.userId
JOIN Products p ON o.productId = p.productId
WHERE u.username = 'Anish' ;


delete from users where userId=1;

drop table orders;

delete from Orders where orderId=7;

