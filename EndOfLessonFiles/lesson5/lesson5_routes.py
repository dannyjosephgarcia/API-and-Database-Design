from flask import Blueprint
import logging
from multiply_two_numbers import MultiplyTwoNumbers
from dependency_injector.wiring import Provide, inject
from lesson5_container import Container

home_route_blueprint = Blueprint("home_route_blueprint", __name__)


@home_route_blueprint.route("/home")
@inject
def direct_to_homepage(multiply_two_numbers=Provide[Container.multiply_two_numbers]):
    logging.info(f"The {direct_to_homepage.__name__} route has started")
    product_outcome = multiply_two_numbers.multiply_two_numbers(2, 3)
    test_string = f"The product result is {product_outcome}"
    logging.info(f"The {direct_to_homepage.__name__} route has ended")
    return test_string
