product"""The product table."""
import datetime
from .. import DB


class Product(DB.Model):
    """
    product Table.

    productid: Integer, Unique identifier for a product.
    companyid: Integer, Unique identifier for a product.
    title: Text, Name of the product
    category: Text, Category of the product.
    """

    __tablename__ = 'product'
    date = DB.Column(DB.DateTime, nullable=False,
                     default=datetime.datetime.utcnow)
    productid = DB.Column(DB.Integer, nullable=False, primary_key=True)
    companyid = DB.Column(DB.Text, nullable=False)
    title = DB.Column(DB.Text, nullable=False)
    category = DB.Column(DB.Text, nullable=False)
