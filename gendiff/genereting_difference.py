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

def format_to_string(dic, indent=4):
    result = []
    for key, value in dic.items():

        if isinstance(value, dict):
            value = format_to_string(value, indent+4)

        if key.startswith('+') or key.startswith('-'):
            result.append(f'{" " * (indent-2)}{key}: {value}')
        else:
            result.append(f'{" " * indent}{key}: {value}')

    result_string = '\n'.join(result)
    return f'{{\n{result_string}\n{" " * (indent-4)}}}'




# def comparing(file1, file2, indent=2):
#     keys = sorted(file1.keys() | file2.keys())
#     result = []
#     indentation = ' '*indent
#     for key in keys:
#         if key not in file2:
#             result.append(f'{" "*indent}- {key}: {to_string(file1[key])}')
#         elif key not in file1:
#             result.append(f'{indentation}+ {key}: {to_string(file2[key])}')
#         elif file1[key] == file2[key]:
#             result.append(f'{indentation}  {key}: {to_string(file1[key])}')
#         elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
#             result.append(
#                 f'{indentation}  {key}: {comparing(file1[key], file2[key], indent+4)}')
#         else:
#             result.extend([f'{indentation}- {key}: {to_string(file1[key])}',
#                            f'{indentation}+ {key}: {to_string(file2[key])}'])
#     # print(result)
#     result_string = '\n'.join(result)
#     return f'{{\n{result_string}\n{" "*(indent-2)}}}'
#     # return result


def comparing(file1, file2):
    keys = sorted(file1.keys() | file2.keys())
    result = {}
    for key in keys:
        if key not in file2:
            result[f'- {key}'] = to_string(file1[key])
        elif key not in file1:
            result[f'+ {key}'] = to_string(file2[key])
        elif file1[key] == file2[key]:
            result[f'{key}'] =  to_string(file1[key])
        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            result[f'{key}'] = comparing(file1[key], file2[key])
        else:
            result[f'- {key}'] =  to_string(file1[key])
            result[f'+ {key}'] = to_string(file2[key])
    # result_string = '\n'.join(result)
    # return f'{{\n{result_string}\n}}'
    return result


def generate_diff(file1_path, file2_path):
    file1 = get_file_data(file1_path)
    file2 = get_file_data(file2_path)
    compared_dict = comparing(file1, file2)
    stringed_dict = format_to_string(compared_dict)
    return stringed_dict
