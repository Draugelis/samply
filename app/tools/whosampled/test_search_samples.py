import unittest

import responses

from search_samples import search_samples
from test_data import test_samples_page, test_track_page


class TestSearchSample(unittest.TestCase):

    @responses.activate
    def test_search_samples_sample_page(self):
        responses.get(
            url='https://www.whosampled.com/Nas/N.Y.-State-of-Mind/samples/',
            body=test_samples_page
        )

        self.assertEqual(search_samples('/Nas/N.Y.-State-of-Mind/'), {
                'track': 'Nas - N.Y. State of Mind',
                'samples': [
                    'Mind Rain - Joe Chambers',
                    'Flight Time - Donald Byrd',
                    'N.T. - Kool & the Gang',
                    'Mahogany - Eric B. & Rakim',
                    'Live at the Barbeque - Main Source'
                ]}
        )

    @responses.activate
    def test_search_samples_track_page(self):
        responses.get(
            url='https://www.whosampled.com/Nas/Represent/samples/',
            status=404
        )

        responses.get(
            url='https://www.whosampled.com/Nas/Represent/',
            body=test_track_page
        )

        self.assertEqual(search_samples('/Nas/Represent/'), {
            'track': 'Nas - Represent',
            'samples': [
                'Thief of Bagdad - Lee Erwin',
                'All Night (Drums) - George Clinton'
            ]}
        )
