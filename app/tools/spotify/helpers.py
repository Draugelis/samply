import re


def get_headers(token):
    """Function generating header for using
    with Spotify API

    Args:
        token (str): Spotify access token

    Returns:
        dict: Headers for HTTP requests
    """
    return {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }


def parse_track(track_data):
    """Function for parsing track data
    from Spotify API response.
    This function returns only details that are
    used.

    Args:
        search_data (dict): Spotify API response JSON object

    Returns:
        dict: Parsed track details
    """
    return {
        'artist': track_data['artists'][0]['name'],
        'track': track_data['name'],
        'uri': track_data['uri']
    }


def get_track_id(query):
    """Function for checking track id
    from Spotify url.

    Args:
        query (str): Search query

    Returns:
        str: track id
    """
    re_pattern = 'https:\/\/open\.spotify\.com\/track\/(\w+)'  # noqa: W605
    re_track_id = re.match(re_pattern, query)

    if re_track_id:
        return re_track_id.groups()[0]
    return False
