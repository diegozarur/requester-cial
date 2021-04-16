from typing import List, Text
import glob


class CustomFileOpen:
    def __init__(self):
        self.__filename = self.__find_websites_file()
        self.__read_file()

    def get_content_in_list(self) -> List:
        return [line.strip() for line in self.__content_file.readlines()]

    def __read_file(self) -> None:
        self.__content_file = open(self.__filename, 'r')

    def __find_websites_file(self) -> Text:
        get_list_of_files_in_txt = glob.glob(r'/code/*.txt')

        for file_path in get_list_of_files_in_txt:
            if 'requirements' not in file_path:
                return file_path

        raise Exception('No file with websites was found!')
