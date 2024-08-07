#!/usr/bin/python3
"""
'states.py' is the view for 'State Objects'
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/states')
def get_all_states():
    """Returns a list of all the State Objects in storage"""
    all_states = [obj.to_dict() for obj in list(storage.all("State").values())]
    return (jsonify(all_states), 200)
