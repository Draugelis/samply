import unittest

from .helpers import parse_track, get_headers, get_track_id
from .test_data import track_search_results


class TestHelpers(unittest.TestCase):
    def test_get_headers(self):
        self.assertEqual(get_headers('1234567890'), {
            'Authorization': 'Bearer 1234567890',
            'Content-Type': 'application/json'
        })

    def test_parse_track(self):
        self.assertEqual(parse_track(track_search_results['tracks']['items'][0]), {
            'artist': 'Nas',
            'track': 'N.Y. State of Mind',
            'uri': 'spotify:track:0trHOzAhNpGCsGBEu7dOJo'
        })

    def test_get_track_id(self):
        track_url = 'https://open.spotify.com/track/0RDm6nifR4k5mHUpX3ZDq7'
        track_id = '0RDm6nifR4k5mHUpX3ZDq7'
        self.assertEqual(get_track_id(track_url), track_id)
        self.assertFalse(get_track_id('Nas N.Y. State of Mind'))
