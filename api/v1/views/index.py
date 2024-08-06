#!/usr/bin/python3
"""
'index'
"""
from api.v1.views import app_views
from flask import jsonify


# Route definitions

@app_views.route("/status", strict_slashes=False)
def get_status():
    """Return a JSON response describing the Web app status."""
    return jsonify({"status": "OK"})
