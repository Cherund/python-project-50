from gendiff.parser import parse
from gendiff.styles import plain, stylish
import os


def get_file_data(file_path):
    extension = os.path.splitext(file_path)[1]
    with open(file_path) as file:
        return parse(file, extension)


def formatted_dict(dic, style):
    if style == 'plain':
        return plain(dic)
    return stylish(dic)

def comparing(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    result = {}
    for key in keys:
        if key not in file2:
            result[key]= {'type': 'removed', 'value': file1[key]}
        elif key not in file1:
            result[key]= {'type': 'added', 'value': file2[key]}
        elif file1[key] == file2[key]:
            result[key] = {'type': 'unchanged','value': file1[key]}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = {'type':'dictionary','value': comparing(file1[key], file2[key])}
        else:
            result[key] = {'type': 'updated', 'value1': file1[key],
                           'value2': file2[key]}
    return result


def generate_diff(file1_path, file2_path, style='stylish'):
    file1 = get_file_data(file1_path)
    file2 = get_file_data(file2_path)
    compared_dict = comparing(file1, file2)
    stringed_dict = formatted_dict(compared_dict, style)
    return stringed_dict
