import time

from datetime import datetime

from CSV.controller import CSVController
from IMDB.controller import get_imdb_results
from constants import replace, INDEX_FILE_NAME
from file.controller import get_all_files
from tqdm import *


def main():
    """
    The main method
    :return:
    """
    print("Hello")
    print("Welcome to MovieTagger")
    dir_path = raw_input("Please enter the folder path to index\n")
    files = get_all_files(dir_path)

    print("Indexing.....")

    csv_interface = CSVController()

    if not dir_path.endswith('/'):
        dir_path += '/'

    csv_interface.initialize_file(dir_path + INDEX_FILE_NAME)

    for file_name in tqdm(files):
        file_extension = file_name.split('.')[-1]
        movie_name = file_name.split('/')[-1].rsplit('.', 1)[0]

        if file_extension in ['mp4', 'mkv', 'avi'] and movie_name != 'Sample':
            formatted_movie_name = format_movie_name(movie_name)
            movie_details = get_imdb_results(formatted_movie_name)
            csv_interface.add_entry(movie_details)

        time.sleep(3)

    csv_interface.close_file()
    csv_interface.remove_duplicate_entries()

    print("Indexing Complete")

def format_movie_name(movie_name):
    """
    Formats the file name to get the name of the movie
    :param movie_name: Name of the movie
    :return:
    """

    formatted_movie_name = movie_name
    for value in replace:
        formatted_movie_name = formatted_movie_name.replace(value, " ")

    today = datetime.today()

    for y in range(1900, int(today.year)):
        if str(y) in formatted_movie_name:
            formatted_movie_name = formatted_movie_name.replace(str(y), " ")

    return formatted_movie_name


if __name__ == "__main__":
    main()