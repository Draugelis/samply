import json
import unittest

import responses

from .add_tracks import add_tracks


class TestAddTracks(unittest.TestCase):
    @responses.activate
    def test_add_tracks(self):
        mock_response = {
                'snapshot_id': 'someId'
        }
        responses.post(
            url='https://api.spotify.com/v1/playlists/123/tracks/',
            body=json.dumps(mock_response),
            status=201
        )
        tracks = [
            'track1',
            'track2'
        ]
        self.assertEqual(add_tracks('123', tracks, 'someToken'), 'someId')
