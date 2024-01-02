#!/usr/bin/python3
"""Starts a minimal web app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    """displays Hello HBNB"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Displays text in support for C"""
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Displays text in support for python"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route("/number/<int:n>", strict_slashes=False)
def number_display(n):
    """Displays the number the user has input in the route"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays the number n in a HTML page"""
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
