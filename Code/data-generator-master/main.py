from flask import Flask, Response, request
from flask_cors import CORS
import webServiceStream
from DataAccessObject import *
from RandomDealData import *

app = Flask(__name__)
CORS(app)

method=["post"]


@app.route('/checkUsername', methods=["post"])
def checkUsername():
    username = request.form["username"]
    password = request.form["password"]
    print(username)
    print(password)
    dao = DataAccessObject()
    return dao.loginCheck(username, password)

@app.route('/historicData')
def historicData():
    dao = DataAccessObject()
    return dao.GetHistoricData()


@app.route('/')
def index():
    return webServiceStream.index()

@app.route('/testservice')
def testservice():
    return webServiceStream.testservice()

@app.route('/streamTest')
def stream():
    return webServiceStream.stream()

@app.route('/streamTest/sse')
def sse_stream():
     return webServiceStream.sse_stream()



def bootapp():
    #global rdd 
    #rdd = RandomDealData()
    #webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
