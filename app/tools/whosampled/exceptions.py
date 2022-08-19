class TrackSearchError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code

    def __str__(self):
        return f"Track search failed with status {self.status_code}"

class SampleSearchError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code

    def __str__(self):
        return f"Sample search failed with status {self.status_code}"