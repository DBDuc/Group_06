from flask import Flask, Response
from flask_cors import CORS
import webServiceStream
from DataAccessObject import *
from RandomDealData import *

app = Flask(__name__)
CORS(app)


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

# TEST Getting the Generator

# @app.route('/testGenerator')
# def Gen():
#     gen =series()
#     val =str(next(gen))
#     print(val)
#     res = Response(val)
#     return res


# def series():
#     for i in range(1,999):
#         yield i

# ----------------------------------


def bootapp():
    #global rdd 
    #rdd = RandomDealData()
    #webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
