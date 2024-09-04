#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
def get_cities(state_id):
    """Returns the list of all City's objects of a State"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"})
    cities = state.cities
    cities_list = []
    for city in cities:
        cities_list += [city.to_dict()]
    return jsonify(cities_list)


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def get_city(city_id):
    """Returns a City object"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def delete_city(city_id):
    """Deletes a City object"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    storage.delete(city)
    storage.save()
    return jsonify({})


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """Creates a City"""
    state = storage.get(State, state_id)
    if state is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    if 'name' not in data:
        return jsonify({"error": "Missing name"})
    data['state_id'] = state_id
    city = City(**data)
    city.save()
    return make_response(jsonify(city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """Updates a City object"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict())