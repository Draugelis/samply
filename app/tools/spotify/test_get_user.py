import json
import unittest

import responses

from .get_user import get_user
from .test_data import user_results


class TestGetUser(unittest.TestCase):
    @responses.activate
    def test_get_user(self):
        responses.get(
            url='https://api.spotify.com/v1/me/',
            body=json.dumps(user_results)
        )

        self.assertEqual(get_user('123'), '1234567890')
