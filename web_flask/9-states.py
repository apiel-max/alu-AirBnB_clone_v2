#!/usr/bin/python3
"""Script that starts a Flask web application for states and state detail."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Displays an HTML page with a list of all states sorted by name."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    return render_template('9-states.html', states=states, state=None)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Displays an HTML page with cities of a state found by id."""
    state = storage.all(State).get('State.{}'.format(id))
    return render_template('9-states.html', states=None, state=state)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
