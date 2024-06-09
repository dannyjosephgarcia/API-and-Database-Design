from dependency_injector import containers, providers
from multiply_two_numbers import MultiplyTwoNumbers
import yaml


class Container(containers.DeclarativeContainer):
    with open('./EndOfLessonFiles/Lesson6/config.yaml') as file:
        config = yaml.safe_load(file)
    multiply_two_numbers = providers.Singleton(MultiplyTwoNumbers,
                                               config['multiply_number'])
