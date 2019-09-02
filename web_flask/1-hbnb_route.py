#!/usr/bin/python3
' starts a Flask web application '
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def route_1():
    ' routing / '
    return 'Hello HBNB!'


@app.route("/hbnb")
def rout_2():
    ' routing / '
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
