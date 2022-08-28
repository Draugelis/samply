import unittest

import helpers
from test_data import test_samples_page, test_track_page


class TestHelpers(unittest.TestCase):
    def test_path_to_full_name(self):
        mock_track_path = '/Nas/N.Y.-State-of-Mind'
        self.assertEqual(helpers.path_to_full_name(mock_track_path), 'Nas - N.Y. State of Mind')

    def test_scrape_samples_sample_page(self):
        self.assertEqual(helpers.scrape_samples(test_samples_page), [
            'Mind Rain - Joe Chambers',
            'Flight Time - Donald Byrd',
            'N.T. - Kool & the Gang',
            'Mahogany - Eric B. & Rakim',
            'Live at the Barbeque - Main Source'
            ])

    def test_scrape_samples_track_page(self):
        self.assertEqual(helpers.scrape_samples(test_track_page), [
            'Thief of Bagdad - Lee Erwin',
            'All Night (Drums) - George Clinton'
        ])
