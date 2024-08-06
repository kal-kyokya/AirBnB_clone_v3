#!/usr/bin/python3
"""
'index'
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.engine.db_storage import classes


# Route definitions

@app_views.route("/status")
def get_status():
    """Return a JSON response describing the Web app status."""
    return jsonify({"status": "OK"})


@app_views.route("/stats")
def get_stats():
    """Return the number of each objects by type."""
    report = {}

    for cls in classes:
        count = storage.count(cls)
        report[cls.lower()] = count

    return (jsonify(report))
