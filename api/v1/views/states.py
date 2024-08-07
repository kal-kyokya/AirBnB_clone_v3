#!/usr/bin/python3
"""
'states.py' is the view for 'State Objects'
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage


@app_views.route('/states')
def get_all_states():
    """Returns a list of all the State Objects in storage."""
    all_states = [obj.to_dict() for obj in list(storage.all("State").values())]
    return (jsonify(all_states), 200)


@app_views.route('/states/<state_id>')
def get_state(state_id):
    """Returns a State instance based on its ID."""
    if state_id:
        state = storage.get("State", state_id)
        if state:
            return (jsonify(state.to_dict()), 200)
    return (abort(404))


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """Deletes a State instance based on its ID."""
    if state_id:
        state = storage.get("State", state_id)
        storage.delete(state)
        storage.save()
        return (jsonify({}), 200)
    return (abort(404))


@app_views.route('states', methods=['POST'])
def create_state():
    """Creates a State instance"""
    data = request.get_json()
    return (jsonify(data))
#    if data.get('content-type') != "application/json":
