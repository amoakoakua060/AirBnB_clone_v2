#!/usr/bin/python3

"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
route /c/<text>: display C followed by the value of the text
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


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
