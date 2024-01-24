#!/usr/bin/python3
'''Importing Flask form flask'''
from flask import Flask

app = Flask(__name__)

@app.route('/',strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb',strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route('/c/<text>',strict_slashes=False)
def ceee(text):
    return "C {}".format(text.replace("_"," "))

@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):
    return "Python {}".format(text.replace("_"," "))

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")