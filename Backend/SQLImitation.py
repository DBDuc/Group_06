import mysql.connector

class SQL(object):

    def __init__(self):
        mysql.connector.connect(host='127.0.0.1',
                                port = "3306",
                                database="mysql-server",
                                user="root",
                                password = "ppp")


    def Query(self,Query):
        print(Query)
        return None



def RequestID(table,column,string):
    sql = SQL()
    return sql.Query("SELECT "+column+
    " FROM "+table+
    " WHERE "+table+"_name = '"+string+"'"
    )

def SetNewRow(table,content):
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

    sql = SQL()

    sql.Query("LOCK TABLES "+table+" WRITE;"+
    "/*!40000 ALTER TABLE "+table+" DISABLE KEYS */;"+
    "INSERT INTO "+table+" "+column_key+" VALUES "+column_value+
    "/*!40000 ALTER TABLE "+table+" ENABLE KEYS */;"+
    "UNLOCK TABLES;"
    )
