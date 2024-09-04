#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def get_reviews(place_id):
    """Returns the list of all Review objects of a Place"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({"error": "Not found"})
    reviews = place.reviews
    reviews_list = []
    for review in reviews:
        reviews_list += [review.to_dict()]
    return jsonify(reviews_list)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """Returns a Review object"""
    review = storage.get(Review, review_id)
    if review is None:
        return jsonify({"error": "Not found"})
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Deletes a Review object"""
    review = storage.get(Review, review_id)
    if review is None:
        return jsonify({"error": "Not found"})
    storage.delete(review)
    storage.save()
    return jsonify({})


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def post_review(place_id):
    """Creates a Review"""
    place = storage.get(Place, place_id)
    if place is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    if 'user_id' not in data:
        return jsonify({"error": "Missing user_id"})
    user = storage.get(User, data['user_id'])
    if user is None:
        return jsonify({"error": "Not found"})
    if 'text' not in data:
        return jsonify({"error": "Missing text"})
    data['place_id'] = place_id
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """Updates a Review object"""
    review = storage.get(Review, review_id)
    if review is None:
        return jsonify({"error": "Not found"})
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"})
    for key, value in data.items():
        if key not in ['id', 'user_id', 'place_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict())