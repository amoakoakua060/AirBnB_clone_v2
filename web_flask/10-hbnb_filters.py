#!/usr/bin/python3

"""
script starts a Flask web application
listening on 0.0.0.0, port 5000
route /hbnb_filters: display list of states
"""


from flask import Flask
from flask import render_template
import models
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnbFilters():
    """ returns page with filters for states and amenities """
    if models.hbnb_type_storage == "db":
        states = models.storage.all("State").values()
        amenities = models.storage.all("Amenity").values()
    else:
        states = models.storage.all(State).values()
        amenities = models.storage.all(Amenity).values()

    states = sorted(states, key=lambda state: state.name)
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    for state in states:
        state.cities.sort(key=lambda city: city.name)

    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_app(exception=None):
    models.storage.close()


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0")
