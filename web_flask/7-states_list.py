#!/usr/bin/python3
"""Flask web app"""
from flask import Flask, render_template
from models import storage
from models import *


web_app = Flask(__name__)


@web_app.route("/states_list", strict_slashes=False)
def statelists():
    """listing states"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@web_app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
