import requests 
from bs4 import BeautifulSoup

from app.tools.logger import setup_logger
logger = setup_logger(__name__)

class WhoScrapped:
    def __init__(self):
        self._base_url = 'https://whosampled.com'
        self._search_url = 'https://whosampled.com/search/'
        self._headers = {
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
        }

    def search_track(self, track):
        logger.debug('Starting search for %s' % track)
        try:
            params = {
                'q': track
            }
            response = requests.get(self._search_url, headers=self._headers, params=params)
            logger.info('Search request for %s finished. Ended with status %d' % (track, response.status_code,))
            soup = BeautifulSoup(response.text, 'html.parser')
            # Checking if the song was found
            top_hit = soup.findAll('div', {'class': 'topHit'})
            if top_hit:
                # Path to track info page; Structure: /{artist}/{track_name}
                track_path = top_hit[0].a['href'] 
                logger.info('Track %s was found.' % (track,))
                return track_path 
            else:
                logger.warning('Track %s was not found.' % (track,))
        except Exception as e:
            logger.error('Track search failed. Exception: %s' % (e,))

 
    def bulk_search_track(self, tracks):
        logger.debug('Starting bulk track search for %s' % (tracks,))
        search_results = []
        for track in tracks: 
            track_results = self.search_track(track)
            if track_results:
                search_results.append(track_results)
        logger.info('Bulk track search was finished. Tracks found: %d' % (len(search_results),))
        return search_results

    def search_samples(self, track_path):

        # Converting track_path to a human readable track name
        # track_path has a consistent structure `/{artists}/{track_name}/`
        # so we convert to `{artist} - {track_name}` format
        track = ' - '.join(track_path.replace('-',' ').strip('/').split('/'))
        try: 
            logger.debug('Starting sample search for %s' % (track,))
            
            sample_url = self._base_url + track_path + 'samples/'
            response = requests.get(sample_url, headers=self._headers)
            logger.info('Sample request for %s finished. Ended with status %d' % (track, response.status_code,))
            
            # FIXME: Add handling for edge case of song having <3 (or <4?) samples 
            soup = BeautifulSoup(response.text,'html.parser')
            samples = soup.findAll('div', {'class': 'sampleEntry'})
            results = []
            for sample in samples:
                sample_name = sample.findAll('a', {'class': 'trackName'})[0].text
                sample_artist = sample.findAll('span', {'class': 'trackArtist'})[0].a.text   
                results.append({
                        'track': track,
                        'sample': f'{sample_name} - {sample_artist}'
                })
            logger.info('Finished searching samples for %s. Samples found: %d' % (track, len(results),))
            return results
        except Exception as e:
            logger.error('Sample search failed. Exception: %s' % (e,))

    def bulk_search_samples(self, track_paths):
        logger.debug('Starting bulk sample search for %s' % (track_paths,))
        results = []
        for track_path in track_paths: 
            samples = self.search_samples(track_path)
            results.extend(samples)
        logger.info('Bulk sample search was finished. Tracks found: %d' % (len(search_results),))
        return results