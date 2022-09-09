import json
import unittest
from unittest.mock import patch
import responses

from .create_playlist import create_playlist
from .test_data import new_playlist_response, user_results


class TestCreatePlaylist(unittest.TestCase):
    @responses.activate
    def test_create_playlist(self):
        responses.get(
            url='https://api.spotify.com/v1/me/',
            body=json.dumps(user_results)
        )

        responses.post(
            url=f'https://api.spotify.com/v1/users/1234567890/playlists/',
            body=json.dumps(new_playlist_response),
            status=201
        )

        self.assertEqual(create_playlist('someName', 'someDesc', 'someToken'), '1234567890')  # noqa: E501
