from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

@app.route('/bonjour')
def heyhey():
    return '<h1>Bonjour!!!</h1>'


if __name__ == '__main__':
    app.run()
