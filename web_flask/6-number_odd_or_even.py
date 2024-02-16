#!/usr/bin/python3
"""
A script that starts a flask app
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    This function displays “Hello HBNB!”
    """

    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function displays “HBNB”
    """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """

    text = text.replace("_", " ")

    return f"C {text}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is(text):
    """
    display “Python ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """

    text = text.replace("_", " ")

    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_is(n):
    """
    Route for n only if its an integer
    """

    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Route for n only if its an integer using html template
    """

    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even//<int:n>", strict_slashes=False)
def number_is_odd_or_even(n):
    """
    Route for n only if its an integer using html template
    """

    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
