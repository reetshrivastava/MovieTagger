from imdb import IMDb


def get_imdb_results(movie_name):
    """
    Gets the details of a movie from the IMDB API
    :param movie_name: Name of the movie
    :return: Details of the movie in dictionary format
    """

    imdb_interface = IMDb()

    movie_names = imdb_interface.search_movie(movie_name)

    if movie_names:
        movie_id = movie_names[0].movieID
        movie_details = imdb_interface.get_movie(movie_id)
        return movie_details

    return None