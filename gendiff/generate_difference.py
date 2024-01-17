from gendiff.styles import format_diff
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
    data1 = get_file_data(file1_path)
    data2 = get_file_data(file2_path)
    diff_tree = create_difference_tree(data1, data2)
    formatted_diff = format_diff(diff_tree, style)
    return formatted_diff
