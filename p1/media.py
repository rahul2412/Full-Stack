'''
Basic datastructure for storing movie data.
'''

class Movie(object):
    '''
    this class initialises the basic movie details required
    '''
    def __init__(self, title, image_url, youtube_url):
        self.title = title
        self.poster_image_url = image_url
        self.trailer_youtube_url = youtube_url

    def __str__(self):
        return self.title
