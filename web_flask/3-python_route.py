#!/usr/bin/python3
' starts a Flask web application '
from flask import Flask, escape
from sys import argv
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def route_1():
    ' routes / '
    return 'Hello HBNB!'


@app.route("/hbnb")
def route_2():
    ' routes /hbnb '
    return 'HBNB'


@app.route("/c/<text>")
def route_3(text):
    ' route /c/<text> '
    text_v = escape(text).replace("_", " ")
    return 'C %s' % text_v


@app.route("/python/<text>")
@app.route("/python/")
def route_4(text='is cool'):
    ' route /python/(<text>) '
    text_v = escape(text).replace("_", " ")
    return 'Python %s' % text_v

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
