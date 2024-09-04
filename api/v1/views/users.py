#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Returns the list of all User objects"""
    users = storage.all(User)
    users_list = []
    for user in users.values():
        users_list += [user.to_dict()]
    return jsonify(users_list)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Returns a User object"""
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"})
    return jsonify(user.to_dict())


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Deletes a User object"""
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"})
    storage.delete(user)
    storage.save()
    return jsonify({})


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """Creates a User"""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    if 'email' not in data:
        return jsonify({"error": "Missing email"})
    if 'password' not in data:
        return jsonify({"error": "Missing password"})
    user = User(**data)
    user.save()
    return make_response(jsonify(user.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """Updates a User object"""
    user = storage.get(User, user_id)
    if user is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())