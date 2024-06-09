import requests


class DummyAPIService:
    def __init__(self, url):
        self.url = url

    def retrieve_dummy_api_response(self):
        response = requests.get(self.url + '/retrieve', json={'firstName': 'ADAM'})
        return response
