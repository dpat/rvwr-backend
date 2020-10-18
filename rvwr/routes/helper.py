"""Routes for modifying the review table."""

import logging
import argparse
from flask import Flask, jsonify, request, make_response, Blueprint
from twilio import twiml
from sqlalchemy import inspect

from ..errors.badrequest import BadRequest
from ..errors.notfound import NotFound

def collector(command):

    message = 'to send a review, text "review productid score review_message"'
    return make_response(jsonify(message))
