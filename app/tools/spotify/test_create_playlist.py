import unittest

import responses

from create_playlist import create_playlist
from test_data import new_playlist_response


class TestCreatePlaylist(unittest.TestCase):
    @responses.activate
    def test_create_playlist(self):
        user_id = 'someUserId'
        responses.post(
            url=f'https://api.spotify.com/v1/users/{user_id}/playlists',
            body=new_playlist_response
        )

        self.assertEqual(create_playlist('someName', token='someToken'), '1234567890')  # noqa: E501
