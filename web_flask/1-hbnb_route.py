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


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
