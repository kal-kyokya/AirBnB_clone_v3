#!/usr/bin/python3
"""
'states.py' is the view for 'State Objects'
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models import storage
from models.state import State


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

    if request.content_type != "application/json":
        return (abort(400), "Not a JSON")
    if "name" not in data:
        return (abort(400, "Missing name"))

    state = State(**data)
    storage.new(state)
    storage.save()
    return (jsonify(state.to_dict()), 201)


@app_views.route('states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Updates a State instance based on its ID"""
    if state_id:
        data = request.get_json()
        ignore_keys = ["id", "create_at", "updated_at"]
        state = storage.get("State", state_id)

        if request.content_type != "application/json":
            return (abort(400, "Not a JSON"))

        for key, value in data.items():
            if key not in ignore_keys:
                setattr(state, key, value)

        storage.save()
        return (jsonify(state.to_dict()), 200)
    return (abort(404))
