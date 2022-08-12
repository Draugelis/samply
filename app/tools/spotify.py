import requests
import json
import base64

from app.tools.logger import setup_logger
logger = setup_logger(__name__)

class Spotify:
    def __init__(self, token):
        self._base_url = 'https://api.spotify.com/v1'
        self._headers = {
            'Authorization': 'Bearer ' + token,
            'Content-Type': 'application/json'
        }
        
    def search_track(self, track):
        logger.debug('Starting track search for %s' % (track,))
        try:
            search_url = self._base_url + '/search'
            params = {
                'q': track,
                'type': 'track',
                'limit': 1
            }
            response = requests.get(search_url, headers=self._headers, params=params)
            logger.info('Search request for %s finished. Ended with status %d' % (track, response.status_code,))
            search_result = response.json()['tracks']['items'][0]
            result = {
                'artist': search_result['artists'][0]['name'],
                'track': search_result['name'],
                'uri': search_result['uri']
            }
            logger.info('Found track %s' % (result,))
            return result
        except Exception as e:
            logger.error('Track search failed. Exception: %s' % (e,))

    def get_user(self):
        logger.debug('Starting user search.')
        try:
            user_url = self._base_url + '/me'
            user_response = requests.get(user_url, headers=self._headers)
            user_id = user_response.json()['id']
            logger.debug('Finished user found.')
            return user_id
        except Exception as e:
            logger.error('User search failed. Exception: %s' % (e,))
        

    def create_playlist(self, name, description):
        logger.debug('Creating playlist %s' % (name,))
        try:
            user_id = self.get_user()
            playlist_url = f'{self._base_url}/users/{user_id}/playlists'
            payload = json.dumps({
                'name': name,
                'description': description
            })
            response = requests.post(playlist_url, headers=self._headers, data=payload)
            logger.info('Create playlist request for %s finished. Ended with status %d' % (name, response.status_code,))
            playlist_id = response.json()['id']
            logger.info('Created playlist %s; ID: %s' % (name, playlist_id,))
            return playlist_id
        except Exception as e:
            logger.error('Create playlist failed. Exception: %s' % (e,))

    def add_tracks(self, playlist_id, tracks):
        logger.debug('Adding tracks %s to playlist %s' % (tracks, playlist_id))
        try:
            playlist_url = f'{self._base_url}/playlists/{playlist_id}/tracks'
            payload = json.dumps({
                'uris': tracks
            })
            response = requests.post(playlist_url, headers=self._headers, data=payload)
            logger.info('Add tracks request for %s finished. Ended with status %d' % (playlist_id, response.status_code,))
            return response.json()
        except Exception as e:
            logger.error('Add tracks to playlist failed. Exception: %s' % (e,))
