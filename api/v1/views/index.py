#!/usr/bin/python3
"""
'index.py' contains route defintions for the app_views blueprint.
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


# Route definitions

@app_views.route("/status")
def get_status():
    """Return a JSON response describing the Web app status."""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def get_stats():
    """Return the number of each objects by type."""
     report = {"amenities": storage.count(amenities),
               "cities": storage.count(cities),
               "places": storage.count(places),
               "reviews": storage.count(reviews),
               "states": storage.count(states),
               "users": storage.count(users)}

    return (jsonify(report))
