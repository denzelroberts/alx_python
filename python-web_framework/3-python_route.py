'''raghhman'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    return "HBNB"

@app.route('/c/<text>')
def ceee(text):
    text = escape(text).replace("_"," ")
    return "C {}".format(text)

@app.route('/python/')
@app.route('/python/<text>')
def py(text='is cool'):
    return "Python {}".format(text.replace("_"," "))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", strict_slashes=False)