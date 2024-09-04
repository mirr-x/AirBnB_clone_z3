#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models import storage
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity


@app_views.route('/cities/<city_id>/places', methods=['GET'], strict_slashes=False)
def get_places(city_id):
    """Returns the list of all Place objects of a City"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    places = city.places
    places_list = []
    for place in places:
        places_list += [place.to_dict()]
    return jsonify(places_list)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_place(place_id):
    """Returns a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({"error": "Not found"})
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'], strict_slashes=False)
def delete_place(place_id):
    """Deletes a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({"error": "Not found"})
    storage.delete(place)
    storage.save()
    return jsonify({})


@app_views.route('/cities/<city_id>/places', methods=['POST'], strict_slashes=False)
def post_place(city_id):
    """Creates a Place"""
    city = storage.get(City, city_id)
    if city is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    if 'user_id' not in data:
        return jsonify({"error": "Missing user_id"})
    user = storage.get(User, data['user_id'])
    if user is None:
        return jsonify({"error": "Not found"})
    if 'name' not in data:
        return jsonify({"error": "Missing name"})
    data['city_id'] = city_id
    place = Place(**data)
    place.save()
    return make_response(jsonify(place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """Updates a Place object"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    for key, value in data.items():
        if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict())


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def post_places_search():
    """Searches for Place objects"""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    places = storage.all(Place).values()
    if 'states' in data:
        places = [place for place in places if place.city.state_id in data['states']]
    if 'cities' in data:
        places = [place for place in places if place.city_id in data['cities']]
    if 'amenities' in data:
        places = [place for place in places if all(amenity.id in data['amenities']
                                                   for amenity in place.amenities)]
    places_list = []
    for place in places:
        places_list += [place.to_dict()]
    return jsonify(places_list)