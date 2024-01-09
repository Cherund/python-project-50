from gendiff.parser import parse
import os


def to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def get_file_data(file_path):
    extension = os.path.splitext(file_path)[1]
    with open(file_path) as file:
        return parse(file, extension)


# def stylish(dic, indent=4):
#     result = []
#     for key, value in dic.items():
#
#         if isinstance(value, dict):
#             value = stylish(value, indent + 4)
#
#         if key.startswith('+') or key.startswith('-'):
#             result.append(f'{" " * (indent-2)}{key}: {value}')
#         else:
#             result.append(f'{" " * indent}{key}: {value}')
#
#     result_string = '\n'.join(result)
#     return f'{{\n{result_string}\n{" " * (indent-4)}}}'


# def comparing(file1, file2):
#     keys = sorted(file1.keys() | file2.keys())
#     result = {}
#     for key in keys:
#         if key not in file2:
#             result[f'- {key}'] = to_string(file1[key])
#         elif key not in file1:
#             result[f'+ {key}'] = to_string(file2[key])
#         elif file1[key] == file2[key]:
#             result[f'{key}'] = to_string(file1[key])
#         elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
#             result[f'{key}'] = comparing(file1[key], file2[key])
#         else:
#             result[f'- {key}'] = to_string(file1[key])
#             result[f'+ {key}'] = to_string(file2[key])
#     return result


def check_for_dict(value, indent):
    if isinstance(value, dict):
        return stylish(value, indent + 4)
    return value


def stylish(dic, indent=2):
    result = []
    for key, value in dic.items():


        if value['type'] == 'deleted':
            result.append(f'{" " * (indent)}- {key}: {value["value"]}')
        elif value['type'] == 'added':
            result.append(f'{" " * (indent)}+ {key}: {value["value"]}')
        elif value['type'] == 'updated':
            result.append(f'{" " * (indent)}- {key}: {value["value1"]}')
            result.append(f'{" " * (indent)}+ {key}: {value["value2"]}')
        elif value['type'] == 'unchanged':
            result.append(f'{" " * indent}  {key}: {value["value"]}')
        else:
            result.append(f'{" " * indent}  {key}: {stylish(value["value"], indent+4)}')


    result_string = '\n'.join(result)
    return f'{{\n{result_string}\n{" " * (indent-2)}}}'


    result_string = '\n'.join(result)
    return f'{{\n{result_string}\n{" " * (indent-2)}}}'


def comparing(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    result = {}
    for key in keys:
        if key not in file2:
            result[key]= {'type': 'deleted', 'value': to_string(file1[key])}
        elif key not in file1:
            result[key]= {'type': 'added', 'value': to_string(file2[key])}
        elif file1[key] == file2[key]:
            result[key] = {'type': 'unchanged','value': to_string(file1[key])}
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[key] = {'type':'dictionary','value': comparing(file1[key], file2[key])}
        else:
            result[key] = {'type': 'updated', 'value1': to_string(file1[key]),
                           'value2': to_string(file2[key])}
    return result


def generate_diff(file1_path, file2_path, style=stylish):
    file1 = get_file_data(file1_path)
    file2 = get_file_data(file2_path)
    compared_dict = comparing(file1, file2)
    stringed_dict = style(compared_dict)
    return stringed_dict
