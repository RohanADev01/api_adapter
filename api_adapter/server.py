"""
Endpoints that allows for the user to use the buttons:
    - create
    - render
    - send
    - login
    - log out
    - sign up
"""

from flask import Flask, request
import json

from api_adapter.auth import signup
from api_adapter.create import signup
from api_adapter.database import db_cleanup

APP = Flask(__name__)


@APP.route("/")
def default_route():
    return "Hello, World!"


@APP.route("/signup", methods=["POST"])
def signup_route():
    body = request.get_json()
    response = signup(body)
    return response

@APP.route("/create", methods=["POST"])
def signup_route():
    body = request.get_json()
    response = signup(body["invoice_details"])
    return json.dumps(response)

@APP.route("/cleanup", methods=["POST"])
def cleanup_route():
    # DEV ONLY ROUTE SHOULD
    # FIND A WAY TO REMOVE IN PROD
    users_val, logged_in_val = db_cleanup()
    res = {
        "msg": f"Removed #{users_val} entries from users and #{logged_in_val} entries from logged_in."
    }
    return res
