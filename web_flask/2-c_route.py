#!/usr/bin/python3
"""
A script that starts a flask app and /hbnb returns “HBNB”
"""

from flask import Flask

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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
