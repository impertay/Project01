from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('about'))

@app.route('/hello')
def about():
    return 'Hello, World!'

@app.route('/hello/CarloVarese')
def id1():
    return 'Hello, CarloVarese'

@app.route('/hello/Oleg')
def id2():
    return 'Hello, Oleg'

if __name__ == '__main__':
    app.run()
