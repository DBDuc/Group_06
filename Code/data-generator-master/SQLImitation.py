import mysql.connector

class SQL(object):

    def __init__(self):
        self.mydb = mysql.connector.connect(host='localhost',
                                #port = "3306",
                                database="db_grad_cs_1917",
                                user="root",
                                password = "ppp")
        self.cur = self.mydb.cursor()


    def SetQuery(self,Query):
        self.cur.execute(Query)
        self.mydb.commit()

    def GetQuery(self,Query):
        self.cur.execute(Query)
        return self.cur.fetchall()

sql = SQL()

def RequestID(table,column,string):
    id = sql.GetQuery("SELECT "+table+"_id"+
    " FROM "+table+
    " WHERE "+table+"_name = '"+string+"'"
    )

    if id == []:
        return None
    else:
        return id[0][0]


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

    sql.SetQuery("LOCK TABLES "+table+" WRITE;")
    sql.SetQuery("/*!40000 ALTER TABLE "+table+" DISABLE KEYS */;")
    sql.SetQuery("INSERT INTO "+table+" "+column_key+" VALUES "+column_value+";")
    sql.SetQuery("/*!40000 ALTER TABLE "+table+" ENABLE KEYS */;")
    sql.SetQuery("UNLOCK TABLES;")
    
