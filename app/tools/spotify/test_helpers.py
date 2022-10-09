import unittest

from .helpers import get_headers, get_playlist_url, get_track_id, parse_track
from .test_data import track_search_results


class TestHelpers(unittest.TestCase):
    def test_get_headers(self):
        self.assertEqual(get_headers('1234567890'), {
            'Authorization': 'Bearer 1234567890',
            'Content-Type': 'application/json'
        })

    def test_parse_track(self):
        track = track_search_results['tracks']['items'][0]
        self.assertEqual(parse_track(track), {
            'artist': 'Nas',
            'track': 'N.Y. State of Mind',
            'id': '0trHOzAhNpGCsGBEu7dOJo'
        })

    def test_get_track_id(self):
        track_url = 'https://open.spotify.com/track/0RDm6nifR4k5mHUpX3ZDq7'
        track_id = '0RDm6nifR4k5mHUpX3ZDq7'
        self.assertEqual(get_track_id(track_url), track_id)
        self.assertFalse(get_track_id('Nas N.Y. State of Mind'))

    def test_get_playlist_url(self):
        playlist_url = 'https://open.spotify.com/playlist/123'
        self.assertEqual(get_playlist_url('123'), playlist_url)
