#!/usr/bin/python3
"""Flask web app"""
from flask import Flask, render_template


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


@web_app.route("/number/<int:n>", strict_slashes=False)
def intpage(n):
    """integer page"""
    return "{:d} is a number".format(n)


@web_app.route("/number_template/<int:n>", strict_slashes=False)
def numberpage(n):
    """Number template page"""
    return render_template("5-number.html", n=n)


@web_app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def oddevenpage(n):
    """odd or even template page"""
    if n % 2 == 0:
        oddoreven = "even"
    else:
        oddoreven = "odd"
    return render_template(
        "6-number_odd_or_even.html", n=n, oddoreven=oddoreven)


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
