#!/usr/bin/python3

"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
route /number/<n>: display n is a number only if n is an integer
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ returns a string """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns a string """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cText(text):
    """ returns a string """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonText(text="is cool"):
    """ returns a string """
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def isNum(n):
    """ returns a number """
    return f"{n} is a number"


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
