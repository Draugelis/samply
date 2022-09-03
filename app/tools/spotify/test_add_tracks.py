import unittest

import responses

from add_tracks import add_tracks


class TestAddTracks(unittest.TestCase):
    @responses.activate
    def test_add_tracks(self):
        responses.post(
            url='https://api.spotify.com/v1/playlists/1234567890/tracks',
            body={
                'snapshot_id': 'someId'
            }
        )
        tracks = [
            'track1',
            'track2'
        ]
        self.assertEqual(add_tracks('123', tracks, 'someToken'), 'someId')
