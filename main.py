from file.controller import get_all_files


def main():
    print("Hello")
    print("Welcome to MovieTagger")
    dir_path = raw_input("Please enter the folder path to index\n")
    files = get_all_files(dir_path)
    print(files)

if __name__ == "__main__":
    main()