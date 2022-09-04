import unittest

import helpers
from test_data import track_search_results


class TestHelpers(unittest.TestCase):
    def test_get_headers(self):
        self.assertEqual(helpers.get_headers('1234567890'), {
            'Authorization': 'Bearer 1234567890',
            'Content-Type': 'application/json'
        })

    def test_parse_track(self):
        self.assertEqual(helpers.parse_track(track_search_results), {
            'artist': 'Nas',
            'track': 'N.Y. State of Mind',
            'uri': 'spotify:track:0trHOzAhNpGCsGBEu7dOJo'
        })

    def test_get_track_id(self):
        track_url = 'https://open.spotify.com/artist/20qISvAhX20dpIbOOzGK3q'
        track_id = '20qISvAhX20dpIbOOzGK3q'
        self.assertEqual(helpers.get_track_id(track_url), track_id)
        self.assertFalse(helpers.get_track_id('Nas N.Y. State of Mind'))
