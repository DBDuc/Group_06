import numpy, random
import json, ast
import SQLImitation as SQL
import mysql.connector
from mysql.connector import Error
from RandomDealData import *
from datetime import datetime, timedelta
from flask import Flask, Response
from flask_cors import CORS

class DataAccessObject:

    def addDealData(self, data):
        """Add Stream Data to SQL DB"""

        data = ast.literal_eval(data)
        Counterparty_id = self.GetSetID ("counterparty",data["cpty"])
        Instrument_id = self.GetSetID ("instrument", data["instrumentName"])

        SQL.SetNewRow("deal",
                    {"deal_time":data["time"],
                    "deal_counterparty_id":Counterparty_id,
                    "deal_instrument_id":Instrument_id,
                    "deal_type":data["type"],
                    "deal_quantity":data["quantity"],
                    "deal_amount":data["price"]
                    })

    def GetSetID(self,table,name):
        """Getter for id object (in case format are tablename_id and table_name)
        Create new entry if no table_name exists"""

        ID = SQL.RequestID(table,table+"_name",name)   
        if ID == None: # To check what SQL.RequestID return in case of no match
            SQL.SetNewRow(table,
                            {table+"_name":name
                            })
            ID = SQL.RequestID(table,table+"_name",name)
        return ID
    
    def connectToDatabase(self):
        connection = None
        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="ppp")
            print("Connection to my DB Successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection
    
    def printDatabases(self, connection):
        cur = connection.cursor()
        cur.execute("SHOW DATABASES")
        databases = cur.fetchall()

        for database in databases:
            print(database)

# Just to test that connection works
if __name__ == "__main__":
      dao = DataAccessObject()
      connection = dao.connectToDatabase()
      dao.printDatabases(connection)
