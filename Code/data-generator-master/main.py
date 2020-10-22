from flask import Flask, Response
from flask_cors import CORS
import webServiceStream
from DataAccessObject import *
from RandomDealData import *

app = Flask(__name__)
CORS(app)

method=["post"]


@app.route('/checkUsername', method=["post"])
def index():
    username = request.form["username"]
    password = request.form["username"]
    dao = DataAccessObject()
    return dao.loginCheck(user, password)


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
