from dependency_injector import containers, providers
from sakila_db_connector import SakilaDBConnector


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['./config.yaml'])
    sakila_db_connector = providers.Singleton(SakilaDBConnector,
                                              config.database.username,
                                              config.database.password,
                                              config.database.host,
                                              config.database.database_name)
