import unittest

import responses

from search_track import search_track
from test_data import track_search_results


class TestSearchTrack(unittest.TestCase):
    @responses.actviate
    def test_search_track(self):
        responses.get(
            url='https://api.spotify.com/v1/search?q=nas%20ny%20state%20of%20mind&type=track&limit=1',  # noqa: E501
            body=track_search_results
        )

        track = 'nas state of mind'
        self.assertEqual(search_track(track, 'someToken'), {
                'artist': 'Nas',
                'track': 'N.Y. State of Mind',
                'uri': 'spotify:track:0trHOzAhNpGCsGBEu7dOJo'
            })
