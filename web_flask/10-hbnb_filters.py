#!/usr/bin/python3
"""Script that starts a Flask web application with HBNB filters page."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays the HBNB filters page with states and amenities."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
