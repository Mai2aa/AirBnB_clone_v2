#!/usr/bin/python3
""" Hello Flask """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def start():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_route(text="is cool"):
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def num_route(n):
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
