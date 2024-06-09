from dependency_injector import containers, providers
from multiply_two_numbers import MultiplyTwoNumbers
from sakila_db_connector import SakilaDBConnector
from dummy_api_service import DummyAPIService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['./config.yaml'])
    multiply_two_numbers = providers.Singleton(MultiplyTwoNumbers,
                                               config.multiply_number,
                                               config.password)

    sakila_db_connector = providers.Singleton(SakilaDBConnector,
                                              config.database.username,
                                              config.database.password,
                                              config.database.host,
                                              config.database.database_name)
    dummy_api_service = providers.Singleton(DummyAPIService,
                                            config.dummy_api.dummy_url)
