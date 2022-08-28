"""Helper functions for whosampled scrapper
"""
from bs4 import BeautifulSoup


def path_to_full_name(track_path):
    """ Converting track path to full name
    track_path has a consistent structure `/{artists}/{track_name}/`
    For full name `{artist} - {track_name}` format is used
    * replace('-', ' ') - for removing '-' delimeter that replaces space

    Args:
        track_path (str): Track path to convert

    Returns:
        str: Readable track name
    """
    return ' - '.join(track_path.replace('-', ' ').strip('/').split('/'))


def scrape_samples(html):
    """Scraping sampled track names
    from a whosampled page.

    Args:
        html (str): Track page to scrape

    Returns:
        list: List of sampled tracks
    """
    soup = BeautifulSoup(html, 'html.parser')
    sample_soup = soup.findAll('section', {'class': ''})[0]
    samples = sample_soup.findAll('div', {'class': 'sampleEntry'})
    sample_list = []
    for sample in samples:
        sample_name = sample.findAll('a', {'class': 'trackName'})[0].text
        sample_artist = sample.findAll('span', {'class': 'trackArtist'})[0].a.text
        sample_list.append(f'{sample_name} - {sample_artist}')

    return sample_list
