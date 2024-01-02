"""Displays state info"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def display_states():
    """Displays all states"""
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('states.html', states=states)

@app.route("/states/<id>", strict_slashes=False)
def display_state(id):
    """Displays a state and its cities"""
    state = storage.get("State", id)
    if state is None:
        return render_template('404.html'), 404
    cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('state.html', state=state, cities=cities)   

@app.teardown_appcontext
def close_session(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=500)
