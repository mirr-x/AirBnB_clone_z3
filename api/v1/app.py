#!/usr/bin/python3

# import sys
# sys.path.append('/home/mirr/Desktop/amir/github/alx/AirBnB_clone_z3')

from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint
from os import getenv
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Not found"})


if __name__ == '__main__':
    HOST = getenv('HBNB_API_HOST', '0.0.0.0')
    PORT = getenv('HBNB_API_PORTx', '5000')
    app.run(host=HOST, port=PORT, threaded=True, debug=True)

