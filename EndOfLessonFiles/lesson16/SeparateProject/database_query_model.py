import logging


class DatabaseQueryModel:
    def __init__(self, request):
        self.validate_database_query_request(request)
        self.first_name = request['firstName']

    def validate_database_query_request(self, request):
        logging.info(f"{self.validate_database_query_request.__name__} has started")
        if 'firstName' not in request:
            raise KeyError("The firstName field is a required field")
        if not isinstance(request['firstName'], str):
            raise TypeError("The firstName field must be of type string")
        logging.info(f"{self.validate_database_query_request.__name__} has ended")
