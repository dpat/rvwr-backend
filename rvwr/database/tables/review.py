"""The review table."""

import datetime
from .. import DB


class Review(DB.Model):
    """
    Review Table.

    reviewid: Integer, Unique identifier for a review.
    productid = Integer, Unique identifier for a review.
    score: Integer, overall score of offering.
    body: Text, The text of the review.
    date: DateTime, Date of the review's creation
    """

    __tablename__ = 'review'
    reviewid = DB.Column(DB.Integer, nullable=False, primary_key=True)
    productid = DB.Column(DB.Integer, nullable=False)
    score = DB.Column(DB.Integer, nullable=False)
    body = DB.Column(DB.Text, nullable=False)
    date = DB.Column(DB.DateTime, nullable=False,
                     default=datetime.datetime.utcnow)
