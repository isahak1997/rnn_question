import os
import datetime


class FileUtill:
    def __init__(self, name=str(datetime.datetime.now()), directory="temp/"):
        self.__filename = name + '.tmp'
        self.__directory = directory
        self.__full_path = self.__directory + self.__filename

    def write_file(self, data):
        with open(self.__full_path, 'w') as file:
            file.write(str(data))

    def drop_file(self):
        os.remove(self.__full_path)

    def read_file(self):
        with open(self.__full_path, 'r') as file:
            data = file.read()
        return data
