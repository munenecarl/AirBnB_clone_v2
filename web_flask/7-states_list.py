"""Displays state info"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def display_states():
    states = storage.all("State").values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def close_session(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=500)
