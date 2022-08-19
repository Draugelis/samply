# Converting track path to full name
# track_path has a consistent structure `/{artists}/{track_name}/`
# For full name `{artist} - {track_name}` format is used
def path_to_full_name(track_path):
    return ' - '.join(track_path.replace('-',' ').strip('/').split('/'))

# Finding samples in a provided page element 
def find_soup_samples(soup):
    samples = soup.findAll('div', {'class': 'sampleEntry'})
    sample_list = []
    for sample in samples:
        sample_name = sample.findAll('a', {'class': 'trackName'})[0].text
        sample_artist = sample.findAll('span', {'class': 'trackArtist'})[0].a.text   
        sample_list.append(f'{sample_name} - {sample_artist}')
    
    return sample_list
