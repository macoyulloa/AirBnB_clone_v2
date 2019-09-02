#!/usr/bin/python3
' starts a Flask web application '
from flask import Flask, escape, render_template
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


@app.route("/number/<int:n>")
def route_5(n):
    ' route to know if there is a number '
    return '%d is a number' % n


@app.route('/number_template/<int:n>')
def route_6(n):
    ' route to know if there is a number in the html '
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def rout_7(n):
    ' route to know if there is a odd or even number in the html '
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
