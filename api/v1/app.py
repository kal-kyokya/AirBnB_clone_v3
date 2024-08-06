#!/usr/bin/python3
"""
'app.py' is a Flask Web app
"""
# Import every needed module and list them in alphabetical order

from api.v1.views import app_views
from flask import Flask, jsonify, Blueprint
from models import storage
from os import getenv


# Specify current file as Flas Web app

app = Flask(__name__)

# register the 'Blueprint' to the Web App

app.register_blueprint(app_views)


# Route definitions

@app.route("/status", strict_slashes=False)
def get_status():
    """Return the status of the Web App"""
    return jsonify({"status": "OK"})


@app.teardown_appcontext
def teardown_appcontext(Exception):
    """End the session"""
    storage.close()


if __name__ == "__main__":
    HOST = getenv("HBNB_API_HOST")
    if not HOST:
        HOST = "0.0.0.0"
    PORT = getenv("HBNB_API_PORT")
    if not PORT:
        PORT = "5000"
    app.run(host=HOST, port=PORT, debug=True)
