"""The review table."""

import datetime
from .. import DB


class Review(DB.Model):
    """
    Review Table.

    reviewid: Integer, Unique identifier for a review.
    productid = Integer, Unique identifier for a review.
    stars: Integer, overall score of offering.
    review: Text, The text of the review.
    date: DateTime, Date of the review's creation
    """

    __tablename__ = 'review'
    reviewid = DB.Column(DB.Integer, nullable=False, primary_key=True)
    stars = DB.Column(DB.Integer, nullable=False)
    review = DB.Column(DB.Text, nullable=False)
    date = DB.Column(DB.DateTime, nullable=False,
                     default=datetime.datetime.utcnow)
    time = DB.Column(DB.Text, nullable=False)
    recurring = DB.Column(DB.Text, nullable=False)
