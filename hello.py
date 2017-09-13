from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return 'Home page'

@app.route('/<username>')
def user_page(username):
    return 'Hello, %s' % username

if __name__ == '__main__':
    app.run()
