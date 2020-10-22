import numpy, random
import json, ast
from MySQLConnect import *
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

        self.SetNewRow("deal",
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

        ID = self.RequestID(table,name)   
        if ID == None: # To check what SQL.RequestID return in case of no match
            self.SetNewRow(table,
                            {table+"_name":name
                            })
            ID = self.RequestID(table,name)
        return ID

    def RequestID(self,table,string):
        """ Getter for id object (in case format are tablename_id and table_name)"""
        id = sql.GetQuery("SELECT "+table+"_id"+
        " FROM "+table+
        " WHERE "+table+"_name = '"+string+"'"
        )

        if id == []:
            return None
        else:
            return id[0][0]


    def SetNewRow(self,table,content):
        """Set new content to "table".
        "content" needs to be in dict format e.g. {column_name:insert_value}"""
        
        column_key = ""
        column_value = ""
        for key,val in content.items():
            column_key += key+","
            if isinstance(val,str): #test for str
                column_value += "'"+str(val)+"',"
            else:
                column_value += str(val)+","

        column_key = "("+column_key[:-1]+")"
        column_value = "("+column_value[:-1]+")"

        sql.SetQuery("LOCK TABLES "+table+" WRITE;")
        sql.SetQuery("/*!40000 ALTER TABLE "+table+" DISABLE KEYS */;")
        sql.SetQuery("INSERT INTO "+table+" "+column_key+" VALUES "+column_value+";")
        sql.SetQuery("/*!40000 ALTER TABLE "+table+" ENABLE KEYS */;")
        sql.SetQuery("UNLOCK TABLES;")
    

    def loginCheck(connection, user, password):
        account = sql.GetQuery('SELECT * FROM users WHERE user_id = "{}" AND user_pwd = "{}"'.format(user, password))
        if account:
            return {"message": "Login successful!",
                    "value": True}
        else:
            return {"message": "Incorrect user/password, try again.",
                    "value": False}


    def printDatabases(self):
        
        databases = sql.GetQuery("SHOW DATABASES")
        for db in databases:
            print(db)
        
        
    

    def printTables(self):
        tables = sql.GetQuery("SHOW TABLES")

        for table in tables:
            print(table)

# Just to test that connection works
if __name__ == "__main__":
    dao = DataAccessObject()
    print(dao.loginCheck("melissa","dbgrad@mel"))
