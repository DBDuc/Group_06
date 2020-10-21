import TestData as TD
import SQLImitation as SQL

#Getter function creat entry when needed
def GetSetID(table,name):
    ID = SQL.RequestID(table,table+"_name",name)   
    if ID == None: # To check what SQL.RequestID return in case of no match
        SQL.SetNewRow(table,
                        {table+"_name":name
                        })
        ID = SQL.RequestID(table,table+"_name",name)
    return ID


def InsertStreamToDataBase (Data):
    Counterparty_id = GetSetID ("counterparty",Data["cpty"])
    Instrument_id = GetSetID ("instrument", Data["instrumentName"])

    SQL.SetNewRow("deal",
                    {"deal_time":Data["time"],
                    "deal_counterparty_id":Counterparty_id,
                    "deal_instrument_id":Instrument_id,
                    "deal_type":Data["type"],
                    "deal_quantity":Data["quantity"],
                    "deal_amount":Data["price"]
                    })



if __name__ == "__main__":
    InsertStreamToDataBase(TD.StreamData)