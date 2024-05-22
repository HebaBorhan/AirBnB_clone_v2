#!/usr/bin/python3
"""Flask web app"""
from flask import Flask, abort, render_template
from models import storage
from models import *
from models.state import State
from models.amenity import Amenity


web_app = Flask(__name__)


@web_app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """HTML with all HBNB details"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    sorted_amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template(
        '10-hbnb_filters.html',
        states=sorted_states, amenities=sorted_amenities)


@web_app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    web_app.run(host="0.0.0.0", port=5000)
