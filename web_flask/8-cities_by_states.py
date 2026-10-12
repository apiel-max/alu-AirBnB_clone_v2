#!/usr/bin/python3
"""Script that starts a Flask web application displaying cities by states."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with states and their cities sorted by name."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
