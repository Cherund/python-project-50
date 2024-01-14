from gendiff.parser import parse
import os


def get_file_data(file_path):
    extension = os.path.splitext(file_path)[1]
    with open(file_path) as file:
        return parse(file, extension[1:])
