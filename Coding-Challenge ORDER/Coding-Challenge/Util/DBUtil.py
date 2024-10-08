# DBUtil.py
import pyodbc

class DBUtil:

    @staticmethod
    def getDBConn():
        try:
            connection = pyodbc.connect('Driver={SQL Server};'
                    'Server=LAPTOP-AT863VNS\SQLEXPRESS;'
                    'Database=Order_Management_System;'
                    'Trusted_Connection=yes;')
            
            # print("DB Connected Successfully")
            return connection
        
        except Exception as error:
            print("Failed to insert into table {}".format(error))

        
