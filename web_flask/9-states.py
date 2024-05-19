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
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('9-states.html', states=sorted_states, state=None)


@web_app.route("/states/<id>", strict_slashes=False)
def statesid(state_id):
    """listing cities of a specific State"""
    state_key = 'State.' + state_id
    states = storage.all(State)
    state = states.get(state_key)
    if state is None:
        return render_template('9-states.html', states=[], state=None, not_found=True)
    return render_template('9-states.html', states=[], state=state, not_found=False)


@web_app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
