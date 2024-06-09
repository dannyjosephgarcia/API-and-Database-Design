from flask import Blueprint, request
import logging
from dependency_injector.wiring import Provide, inject
from lesson13_container import Container

home_route_blueprint = Blueprint("home_route_blueprint", __name__)


@home_route_blueprint.route("/home", methods=['GET'])
@inject
def direct_to_home_page(sakila_db_connector=Provide[Container.sakila_db_connector]):
    logging.info(f"{direct_to_home_page.__name__} has started")
    route_request = request.get_json()
    first_name = route_request['firstName']
    full_name = sakila_db_connector.execute_actor_table_query(first_name=first_name)
    test_string = f"The names of the people returned from our database are: {full_name}"
    logging.info(f"{direct_to_home_page.__name__} has run successfully")
    return test_string
