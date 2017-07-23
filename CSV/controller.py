import csv

import fileinput


class CSVController():
    """

    """

    def initialize_file(self, file_name):
        """
        Creates a CSV file and adds headers
        :param file_name: Name of the file to be created
        :return:
        """
        self.file_name = file_name
        self.file_obj = file(file_name, "w")

        fieldnames = ['Movie Name', 'IMDB Rating', 'Genre']
        self.writer = csv.DictWriter(self.file_obj, fieldnames=fieldnames)

        self.writer.writeheader()

    def close_file(self):
        """

        :return:
        """
        self.file_obj.close()

    def add_entry(self, movie_obj):
        """

        :return:
        """

        if self.writer:
            self.writer.writerow({'Movie Name':movie_obj.get('title'),
                                  'IMDB Rating':movie_obj.get('rating'),
                                  'Genre':",".join(movie_obj.get('genres'))})
        else:
            print("File not created")

    def remove_duplicate_entries(self):
        """

        :return:
        """
        seen = set()
        for line in fileinput.FileInput(self.file_name, inplace=1):
            if line in seen: continue
            seen.add(line)
            print line,