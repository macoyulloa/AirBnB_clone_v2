#!/usr/bin/python3
' starts a Flask web application '
from flask import Flask, escape, render_template
from sys import argv
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def list_state1():
    ' take the list of states '
    all_states = storage.all('State').values()
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def remove_session(var):
    ' remove the current SQLAlchemy Session '
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
