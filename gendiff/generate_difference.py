from gendiff.styles.get_style import style_dict
from gendiff.create_tree import create_difference_tree
from gendiff.parser import parse
import os


def get_extension(file_path):
    extension = os.path.splitext(file_path)[1]
    return extension[1:]


def get_file_data(file_path):
    with open(file_path) as file:
        return parse(file, get_extension(file_path))


def generate_diff(file1_path, file2_path, style='stylish'):
    file1 = get_file_data(file1_path)
    file2 = get_file_data(file2_path)
    compared_dict = create_difference_tree(file1, file2)
    # print(compared_dict)
    stringed_dict = style_dict(compared_dict, style)
    return stringed_dict
