from flask import Flask

app = Flask(__name__)

@app.route('/endpoint1')
def endpoint1():
    return "Received message from endpoint 1"

@app.route('/endpoint2')
def endpoint2():
    return "Received message from endpoint 2"

@app.route('/endpoint3')
def endpoint3():
    return "Received message from endpoint 3"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)