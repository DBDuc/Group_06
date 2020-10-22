from MySQLConnect import *


def getLogin():

    user = input("Please enter your username:")
    password = input("Please enter your password:")

    loginCheck(user, password)


def loginCheck(user, password):
    account = sql.GetQuery('SELECT * FROM users WHERE user_id = "{}" AND user_pwd = "{}"'.format(user,password))
    if account:
        return print ("Login successful!")

    else:
        return print("Incorrect user/password, try again.")


def newLogin():

    sql.SetQuery ("INSERT INTO users (user_id, user_pwd) VALUES ('{}', '{}')".format("melissa", "dbgrad@mel"))
    return print("Sucessfully created new account!")

newLogin()