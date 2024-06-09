from flask import Blueprint
import logging
from dependency_injector.wiring import Provide, inject
from lesson11_container import Container

home_route_blueprint = Blueprint("home_route_blueprint", __name__)


@home_route_blueprint.route("/home", methods=['GET'])
@inject
def direct_to_home_page(sakila_db_connector=Provide[Container.sakila_db_connector]):
    logging.info(f"{direct_to_home_page.__name__} has started")
    first_name = sakila_db_connector.execute_actor_table_query()
    test_string = f"The first name of the first actor returned from the table is {first_name}"
    logging.info(f"{direct_to_home_page.__name__} has run successfully")
    return test_string
