#!/usr/bin/python3

"""
script that starts a Flask web application
web application must be listening on 0.0.0.0, port 5000
route /number_odd_or_even/<n>: display a HTML page only if n is an integer
"""


from flask import Flask, render_template

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
def numText(n):
    """ returns a number """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def numTemplate(n):
    """ returns a number html file """
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddOrEvenTemplate(n):
    """ returns a number html file """
    if n % 2 == 0:
        text = "even"
    else:
        text = "odd"
    return render_template("6-number_odd_or_even.html", text=f"{n} is {text}")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
