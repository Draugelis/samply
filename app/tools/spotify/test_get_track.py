import unittest

import responses

from get_track import get_track
from test_data import track_results


class TestGetTrack(unittest.TestCase):
    @responses.activate
    def test_get_track(self):
        responses.get(
            url='https://api.spotify.com/v1/tracks/0trHOzAhNpGCsGBEu7dOJo',
            body=track_results
        )

        self.assertEqual(get_track('0trHOzAhNpGCsGBEu7dOJo', '123'), {
                'artist': 'Nas',
                'track': 'N.Y. State of Mind',
                'uri': 'spotify:track:0trHOzAhNpGCsGBEu7dOJo'
            })
