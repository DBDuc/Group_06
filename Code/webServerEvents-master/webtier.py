from flask import Flask, render_template, Response
from flask_sse import sse
from flask_cors import CORS
from flask import request
import requests
import time
import json

app = Flask(__name__)
#app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

@app.route('/deals')
def forwardStream():
    r = requests.get('http://localhost:8080/streamTest', stream=True)
    def eventStream():
            for line in r.iter_lines( chunk_size=1):
                if line:
                    yield 'data:{}\n\n'.format(line.decode())
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/client/testservice')
def client_to_server():
    r = requests.get('http://localhost:8080/testservice')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/')
@app.route('/index')
def index():
    return "webtier service points are running..."


""" access web tier end points to check log in credentials"""
@app.route('/login')
def login_credentials():
    r = requests.get('http://localhost:8080/login')
    return True

""" access web tier end points to display historic data"""
@app.route('/historicdeals')
def historic_deals():
    r = requests.get('http://localhost:8080/historicdeals', stream=False)
    return True

""" example deal file """
@app.route('/json_example') #GET requests will be blocked
def json_example():
    data = []
    with open('../../deals_data.json') as json_file:
        data = json.load(json_file)

    return data

def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()


