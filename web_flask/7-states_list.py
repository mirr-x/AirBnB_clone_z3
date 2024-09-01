#!/usr/bin/python3
"""Flask web application"""

import sys
sys.path.append('/home/mirr/Desktop/amir/github/alx/AirBnB_clone_z2')



from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ show states """
    States = storage.all(State)
    return render_template('7-states_list.html', states=States)

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
