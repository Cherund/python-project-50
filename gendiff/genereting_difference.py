from gendiff.cli import get_paths
import json


def to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(args):
    paths = get_paths(args)
    file1 = json.load(open(paths['first_file']))
    file2 = json.load(open(paths['second_file']))
    keys = sorted(file1.keys() | file2.keys())
    result = []
    for key in keys:
        if key not in file2:
            result.append(f'- {key}: {to_string(file1[key])}')
        elif key not in file1:
            result.append(f'+ {key}: {to_string(file2[key])}')
        elif file1[key] == file2[key]:
            result.append(f'  {key}: {to_string(file1[key])}')
        else:
            result.extend([f'- {key}: {to_string(file1[key])}',
                           f'+ {key}: {to_string(file2[key])}'])

    result_string = '\n  '.join(result)
    return f'{{\n  {result_string}\n}}'
