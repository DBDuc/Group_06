from flask import Flask, render_template, Response
from flask_sse import sse
from flask_cors import CORS
from flask import request
from flask import Flask, session, redirect, url_for, request
from markupsafe import escape
import requests
import time
import json

app = Flask(__name__)
#app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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

""" example deal file """
@app.route('/json_example') #GET requests will be blocked
def json_example():
    #data = []
    #with open('../../deals_data.json') as json_file:
    #    data = json.load(json_file)

    API_ENDPOINT = "http://localhost:8080/historicData"
    r = requests.get(url=API_ENDPOINT)
    data = r.json()

    return data


@app.route('/')
@app.route('/index')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['password']

        API_ENDPOINT = "http://localhost:8080/checkUsername"
        #User: alison pw:gradprog2016@07
        #r = requests.post(url=API_ENDPOINT, data={"username": "alison", "password": "gradprog2016@07"})
        #r = requests.post(url=API_ENDPOINT, data={"username": "alison", "password": "gradprog2016@07asd"})

        r = requests.post(url=API_ENDPOINT, data={"username": username, "password": password})
        data = r.json()

        print(data["value"])
        if data["value"]:
            #return redirect(url_for('index'))
            return redirect("http://localhost:3000")
        else:
            return data["message"]

    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''
# LOGIN TESTS
def test_login_positive(client):
    API_ENDPOINT = "http://localhost:8080/checkUsername"
    r = requests.post(url=API_ENDPOINT, data={"username": "alison", "password": "gradprog2016@07"})    
    assert b'Login successful!' in rv["message"]

def test_login_negative(client):
    API_ENDPOINT = "http://localhost:8080/checkUsername"
    r = requests.post(url=API_ENDPOINT, data={"username": "username", "password": "password"})    
    assert b'Incorrect user/password, try again.' in rv["message"]

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))



def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()


