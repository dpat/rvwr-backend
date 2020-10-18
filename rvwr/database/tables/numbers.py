"""The numbers table."""

import datetime
from .. import DB


class Numbers(DB.Model):
    """
    Numbers Table.

    """

    __tablename__ = 'numbers'
    numberid = DB.Column(DB.Integer, nullable=False, primary_key=True)
    number = DB.Column(DB.Text, nullable=False)
