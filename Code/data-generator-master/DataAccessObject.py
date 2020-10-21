from flask import Flask, Response
from flask_cors import CORS
import numpy, random
from datetime import datetime, timedelta
import json, ast
from RandomDealData import *
import SQLImitation as SQL

class DataAccessObject:

    def addData(self, data):
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