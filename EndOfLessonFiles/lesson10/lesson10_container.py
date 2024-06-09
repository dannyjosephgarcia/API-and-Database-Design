from dependency_injector import containers, providers
from multiply_two_numbers import MultiplyTwoNumbers
import yaml


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['./config.yaml'])
    multiply_two_numbers = providers.Singleton(MultiplyTwoNumbers,
                                               config.multiply_number,
                                               config.password)
