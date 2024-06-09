import unittest
from app import app
from unittest.mock import patch
from dummy_api_service import DummyAPIService

DIRECT_TO_HOMEPAGE_URL = "/retrieve"
DIRECT_TO_HOMEPAGE_REQUEST = {"firstName": "ADAM"}
DIRECT_TO_HOMEPAGE_REQUEST_NO_FIRST_NAME = {'blabla': 'blabla'}
DIRECT_TO_HOMEPAGE_REQUEST_WRONG_DATA_TYPE = {'firstName': 1}
DIRECT_TO_HOMEPAGE_RESPONSE = "The names of the people returned from our query are: ADAM GRANT ADAM HOPPER "

DUMMY_API_URL = "/call_dummy_api"


class TestHomeRoutes(unittest.TestCase):
    def test_direct_to_home_page_happy(self):
        response = app.test_client().get(DIRECT_TO_HOMEPAGE_URL, json=DIRECT_TO_HOMEPAGE_REQUEST)
        self.assertEqual(response.json, DIRECT_TO_HOMEPAGE_RESPONSE)
        self.assertEqual(response.status_code, 200)

    def test_direct_to_home_page_no_first_name_field(self):
        response = app.test_client().get(DIRECT_TO_HOMEPAGE_URL, json=DIRECT_TO_HOMEPAGE_REQUEST_NO_FIRST_NAME)
        self.assertEqual(response.status_code, 500)

    def test_direct_to_home_page_wrong_data_type(self):
        response = app.test_client().get(DIRECT_TO_HOMEPAGE_URL, json=DIRECT_TO_HOMEPAGE_REQUEST_WRONG_DATA_TYPE)
        self.assertEqual(response.status_code, 500)

    @patch.object(DummyAPIService, 'retrieve_dummy_api_response', return_value=DIRECT_TO_HOMEPAGE_RESPONSE)
    def test_call_dummy_api_happy(self, mock_dummy_api_response):
        response = app.test_client().get(DUMMY_API_URL)
        self.assertEqual(response.json, DIRECT_TO_HOMEPAGE_RESPONSE)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
