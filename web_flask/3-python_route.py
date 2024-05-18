#!/usr/bin/python3
"""Flask web app"""
from flask import Flask


web_app = Flask(__name__)


@web_app.route("/", strict_slashes=False)
def hellopage():
    """hello page"""
    return "Hello HBNB!"


@web_app.route("/hbnb", strict_slashes=False)
def hbnbpage():
    """hbnb page"""
    return "HBNB"


@web_app.route("/c/<text>", strict_slashes=False)
def Cpage(text):
    """C page"""
    return "C " + text.replace("_", " ")


@web_app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@web_app.route("/python/<text>", strict_slashes=False)
def Pythonpage(text):
    """Python page"""
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
