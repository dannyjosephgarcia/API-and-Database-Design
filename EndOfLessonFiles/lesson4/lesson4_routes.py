from flask import Blueprint
import logging

home_route_blueprint = Blueprint("home_route_blueprint", __name__)


@home_route_blueprint.route("/home")
def direct_to_homepage():
    logging.info(f"The {direct_to_homepage.__name__} route has started")
    test_string = "Welcome to Homepage"
    logging.info(f"The {direct_to_homepage.__name__} route has ended")
    return test_string
