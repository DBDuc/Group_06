import mysql.connector


mydb = mysql.connector.connect(host = "localhost",
                               user="root",
                               password="ppp"
                               )

cur = mydb.cursor()

cur.execute("SHOW DATABASES")
databases = cur.fetchall()

for database in databases:
    print(database)

