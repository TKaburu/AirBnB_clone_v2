#!/usr/bin/python3
"""
A script that starts a flask app and / returns “Hello HBNB!”
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    This function displays “Hello HBNB!”
    """

    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)