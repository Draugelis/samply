import re


def listify(entry):
    return entry if isinstance(entry, list) else [entry]


def clean_track_name(name):
    dirt_pattern = r'( - .+|\(feat.+)'
    clean_name = re.sub(dirt_pattern, '', name)
    return clean_name
