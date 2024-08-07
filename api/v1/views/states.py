#!/usr/bin/python3
"""
'states.py' is the view for 'State Objects'
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage


@app_views.route('/states')
def get_all_states():
    """Returns a list of all the State Objects in storage"""
    all_states = [obj.to_dict() for obj in list(storage.all("State").values())]
    return (jsonify(all_states), 200)

@app_views.route('/states/<state_id>')
def get_state(state_id):
    """Return a State instance based on its ID"""
    if state_id:
        state = storage.get("State", state_id).to_dict()
        return (jsonify(state))
    return (abort(404))
