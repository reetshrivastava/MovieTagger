from os import walk, path


def get_all_files(dir_path):
    """
    Returns all the files in a directory in list format
    :param dir_path: A directory path
    :return: List of files in dir_path
    """
    files = [path.join(dp, f) for dp, dn, filenames in walk(dir_path) for f in filenames]

    return files