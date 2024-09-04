# #!/usr/bin/python3

# from api.v1.views import app_views
# from flask import jsonify, request, make_response
# from models import storage
# from models.place import Place
# from models.amenity import Amenity


# @app_views.route('/places/<place_id>/amenities', methods=['GET'], strict_slashes=False)
# def get_amenities(place_id):
#     """Returns the list of all Amenity objects of a Place"""
#     place = storage.get(Place, place_id)
#     if place is None:
#         return jsonify({"error": "Not found"})
#     amenities = place.amenities
#     amenities_list = []
#     for amenity in amenities:
#         amenities_list += [amenity.to_dict()]
#     return jsonify(amenities_list)


# @app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
# def delete_amenity(place_id, amenity_id):
#     """Deletes an Amenity object"""
#     place = storage.get(Place, place_id)
#     if place is None:
#         return jsonify({"error": "Not found"})
#     amenity = storage.get(Amenity, amenity_id)
#     if amenity is None:
#         return jsonify({"error": "Not found"})
#     if amenity not in place.amenities:
#         return jsonify({"error": "Not found"})
#     storage.delete(amenity)
#     storage.save()
#     return jsonify({})


# @app_views.route('/places/<place_id>/amenities/<amenity_id>', methods=['POST'], strict_slashes=False)
# def post_amenity(place_id, amenity_id):
#     """Creates an Amenity"""
#     place = storage.get(Place, place_id)
#     if place is None:
#         return jsonify({"error": "Not found"})
#     amenity = storage.get(Amenity, amenity_id)
#     if amenity is None:
#         return jsonify({"error": "Not found"})
#     if amenity in place.amenities:
#         return jsonify(amenity.to_dict())
#     place.amenities.append(amenity)
#     storage.save()
#     return jsonify(amenity.to_dict())