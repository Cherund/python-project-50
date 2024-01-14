from gendiff.parser import parse
from gendiff.styles import plain, stylish, json_dumps
from gendiff.create_tree import create_difference_tree
import os


def get_file_data(file_path):
    extension = os.path.splitext(file_path)[1]
    with open(file_path) as file:
        return parse(file, extension)


def formatted_dict(dic, style):
    if style == 'plain':
        return plain(dic)

    if style == 'json':
        return json_dumps(dic)

    return stylish(dic)


def generate_diff(file1_path, file2_path, style='stylish'):
    file1 = get_file_data(file1_path)
    file2 = get_file_data(file2_path)
    compared_dict = create_difference_tree(file1, file2)
    stringed_dict = formatted_dict(compared_dict, style)
    return stringed_dict
