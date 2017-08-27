from media import Movie
import csv

def get_mov_details(files):
    '''
    data is being pulled from csv creating list of objects of movie.
    '''
    movies = []
    with open(files, 'r') as file:
        reader = csv.DictReader(file)
        for movie in reader:
            movies.append(Movie(title=movie['name'], image_url=movie['image_url'], youtube_url=movie['youtube_url']))
    return movies

