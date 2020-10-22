import mysql.connector
from mysql.connector import Error

class SQL(object):

    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host='localhost',
                                    database="db_grad_cs_1917",
                                    user="root",
                                    password = "ppp")
        except Error as e:
            print(f"The error '{e}' occurred")

        self.cur = self.mydb.cursor()


    def SetQuery(self,Query):
        self.cur.execute(Query)
        self.mydb.commit()

    def GetQuery(self,Query):
        self.cur.execute(Query)
        return self.cur.fetchall()

sql = SQL()