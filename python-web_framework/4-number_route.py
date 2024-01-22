"""raghhman"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def hello_hbnb():
    '''documented'''
    return "Hello HBNB!"

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    '''documented'''
    return "HBNB"

@app.route('/c/<text>',strict_slashes=False)
def ceee(text):
    '''documented'''
    return "C {}".format(text.replace("_"," "))

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):
    '''documented'''
    return "Python {}".format(text.replace("_"," "))

'''documented'''
@app.route('/number/', strict_slashes=False)
@app.route('/number/<n>', strict_slashes=False)
def py(n):
    '''documented'''
    if n == int:
        return "{} is a number".format(n)

'''documented'''
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")