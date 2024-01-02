"""Displays state info"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/cities_by_states", strict_slashes=False)
def display_cities_by_states():
	"""Displays cities by their states"""
	states = storage.all("State").values()
	states = sorted(states, key=lambda state: state.name)
	return render_template('8-cities_by_states.html', states=states)   

@app.teardown_appcontext
def close_session(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=500)
