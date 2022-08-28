import unittest

import responses

from search_track import search_track
from test_data import test_search_page_success, test_search_page_not_found


class TestSearchTrack(unittest.TestCase):
    @responses.activate
    def test_searck_track_success(self):
        responses.get(
            url='https://www.whosampled.com/search/?q=Nas+ny+state+of+mind',
            body=test_search_page_success
        )
        test_query = 'Nas ny state of mind'
        self.assertEqual(search_track(test_query), "/Nas/N.Y.-State-of-Mind/")

    @responses.activate
    def test_searck_track_not_found(self):
        responses.get(
            url='https://www.whosampled.com/search/?q=something+I+cant+find',
            body=test_search_page_not_found
        )
        test_query = 'something I cant find'
        self.assertRaises(RuntimeError, search_track(test_query))
