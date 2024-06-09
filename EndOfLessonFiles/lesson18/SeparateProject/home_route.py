from flask import Blueprint, request, jsonify
import logging
from dependency_injector.wiring import Provide, inject
from container import Container
from database_query_model import DatabaseQueryModel

home_route_blueprint = Blueprint("home_route_blueprint", __name__)


@home_route_blueprint.route("/retrieve", methods=['GET'])
@inject
def direct_to_home_page(sakila_db_connector=Provide[Container.sakila_db_connector]):
    logging.info(f"{direct_to_home_page.__name__} has started")
    route_request = request.get_json()
    database_model = DatabaseQueryModel(route_request)
    full_name = sakila_db_connector.execute_actor_table_query(first_name=database_model.first_name)
    test_string = f"The names of the people returned from our query are: {full_name}"
    logging.info(f"{direct_to_home_page.__name__} has run successfully")
    return jsonify(test_string)


