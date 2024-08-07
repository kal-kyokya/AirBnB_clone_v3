#!/usr/bin/python3
"""index file, main view file
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route("/status")
def get_status():
    """Return a JSON response describing the Web app status."""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def get_stats():
    """Return the number of each objects by type."""
    report = {"amenities": storage.count("Amenity"),
              "cities": storage.count("City"),
              "places": storage.count("Place"),
              "reviews": storage.count("Review"),
              "states": storage.count("State"),
              "users": storage.count("User")}

    return (jsonify(report))
