import mysql.connector

mydb = mysql.connector.connect(host = "localhost",
                               user="root",
                               password="ppp",
                               database= "db_grad_cs_1917"
                              )
cur = mydb.cursor()


def getLogin():

    user = input("Please enter your username:")
    password = input("Please enter your password:")

    loginCheck(user, password)


def loginCheck(user, password):

    cur.execute('SELECT * FROM users WHERE user_id = %s AND user_pwd = %s', (user, password))
    account = cur.fetchone()
    if account:
        return print ("Login successful!")

    else:
        return print("Incorrect user/password, try again.")


def newLogin():

    query = "INSERT INTO users (user_id, user_pwd) VALUES (%s, %s)"
    login_details = ("melissa", "dbgrad@mel")
    cur.execute(query, login_details)

    mydb.commit()
    return print("Sucessfully created new account!")