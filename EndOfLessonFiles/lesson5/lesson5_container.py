from dependency_injector import containers, providers
from multiply_two_numbers import MultiplyTwoNumbers


class Container(containers.DeclarativeContainer):
    multiply_two_numbers = providers.Singleton(MultiplyTwoNumbers)
