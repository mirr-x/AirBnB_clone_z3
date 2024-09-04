#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """Returns the list of all Amenity objects"""
    amenities = storage.all(Amenity)
    amenities_list = []
    for amenity in amenities.values():
        amenities_list += [amenity.to_dict()]
    return jsonify(amenities_list)


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """Returns a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return jsonify({"error": "Not found"})
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """Deletes a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return jsonify({"error": "Not found"})
    storage.delete(amenity)
    storage.save()
    return jsonify({})


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """Creates a Amenity"""
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    if 'name' not in data:
        return jsonify({"error": "Missing name"})
    amenity = Amenity(**data)
    amenity.save()
    return make_response(jsonify(amenity.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """Updates a Amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict())