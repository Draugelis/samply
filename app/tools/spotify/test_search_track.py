import json
import unittest

import responses

from .search_track import search_track
from .test_data import track_search_results


class TestSearchTrack(unittest.TestCase):
    @responses.activate
    def test_search_track(self):
        responses.get(
            url='https://api.spotify.com/v1/search/?q=nas+state+of+mind&type=track',  # noqa: E501
            body=json.dumps(track_search_results)
        )

        track = 'nas state of mind'
        self.assertEqual(search_track(track, 'someToken'), {
                'artist': 'Nas',
                'track': 'N.Y. State of Mind',
                'uri': 'spotify:track:0trHOzAhNpGCsGBEu7dOJo'
            })
