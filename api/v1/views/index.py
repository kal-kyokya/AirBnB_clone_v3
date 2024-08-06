#!/usr/bin/python3
"""
'index'
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
    obj_list = list(storage.all().values())
    report = {}
    classes = []

    for obj in obj_list:
        if obj.__class__.__name__ in classes:
            pass
        else:
            classes.append(obj.__class__.__name__)
    for cls in classes:
        count = storage.count(cls)
        report[cls] = count

    return (jsonify(report))
