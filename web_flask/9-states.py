#!/usr/bin/python3
"""Flask web app"""
from flask import Flask, abort, render_template
from models import storage
from models import *
from models.state import State


web_app = Flask(__name__)


@web_app.route("/states", strict_slashes=False)
def mystates():
    """listing  all State objects"""
    sorted_states = storage.all(State).values()
    return render_template('9-states.html', states=sorted_states)


@web_app.route("/states/<id>", strict_slashes=False)
def statesid():
    """listing cities of a specific State"""
    state = storage.all(State).get(f'State.{id}')
    if state is None:
        abort(404)
    return render_template('9-states.html', state=state)


@web_app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
