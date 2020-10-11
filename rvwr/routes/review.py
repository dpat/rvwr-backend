"""Routes for modifying the review table."""

import logging
import argparse
from flask import Flask, jsonify, request, make_response, Blueprint
from twilio import twiml
from sqlalchemy import inspect

from ..helpers.bphandler import BPHandler
from ..database import DB
from ..database.utils import add_value, table2dict
from ..database.tables.review import Review
from ..errors.badrequest import BadRequest
from ..errors.notfound import NotFound


REVIEW_BP = Blueprint('review', __name__)
BPHandler.add_blueprint(REVIEW_BP)


def handler(command):

    if command[0][0] == '-':
        if command[0][:5] == '-get=':
            review_id = command[0][5:]
            return get_review(review_id)
        if command[0][:8] == '-delete=':
            review_id = command[0][8:]
            return delete_review(review_id)
    else:
        product = command[0]
        score = command[1]
        review = command[2:]

        return add_review(product, score, review)


def add_review(product, score, review):
    """Add a single review to the database."""

    message = ' '.join(message)
    review = {}
    values = {'product': product, 'score': score, 'review': review}
    for field in values.keys():
        if field in inspect(Review).mapper.column_attrs:
            review[field] = values[field]

    new = Review(**review)
    add_value(new)

    return make_response(jsonify(table2dict(new)), 201)


def get_review(id):
    """Get a single review based on the review id, optionally
       return all reviews if id=all"""

    if id == 'all':
        list_of_reviews = []
        reviews = Reviews.query.all()
        for review in reviews:
            list_of_reviews.append(table2dict(review))
        return make_response(jsonify(list_of_reviews), 200)
    else:
        review_id = int(id)
        review = query_reviewid(review_id)
        return make_response(jsonify(table2dict(review)), 200)


def delete_review(id):
    """Drop a review from the database"""

    review_id = int(id)
    review = query_reviewid(review_id)
    DB.session.delete(review)

    DB.session.commit()
    message = "review number (" + str(review_id) + ") deleted"
    return make_response(jsonify(message), 204)


def query_reviewid(review_id):
    """
    Get a review based on the reviewid or raise a BadRequest when not found

    :param post_id: int, primary key for the post.
    :return: Table row representing a post.
    """
    review = Review.query.filter_by(reviewid=review_id).first()
    if not review:
        raise NotFound('review not found')
        return 'review not found'
    return review
