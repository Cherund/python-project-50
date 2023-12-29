import json
from pathlib import Path


def to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def generate_diff(args):
    file1 = json.load(open(args.first_file))
    file2 = json.load(open(args.second_file))
    # file1 = json.load(open(args[0]))
    # file2 = json.load(open(args[1]))
    keys = sorted(file1.keys() | file2.keys())
    print(file1)
    result = []
    for key in keys:
        if key not in file2:
            result.append(f'- {key}: {file1[key]}')
        elif key not in file1:
            result.append(f'+ {key}: {to_string(file2[key])}')
        elif file1[key] == file2[key]:
            result.append(f'  {key}: {to_string(file1[key])}')
        else:
            result.extend([f'- {key}: {to_string(file1[key])}',
                           f'+ {key}: {to_string(file2[key])}'])

    result_string = '\n  '.join(result)
    print(f'{{\n  {result_string}\n}}')


# def generate_diff(args):
#     # file1 = json.load(open(args.first_file))
#     # file2 = json.load(open(args.second_file))
#     file1 = json.load(open(args[0]))
#     file2 = json.load(open(args[1]))
#     merged_files = dict(sorted((file1 | file2).items()))
#     print(merged_files)
#     print(file1)
#     print(file2)
#     result = {}
#     for key, value in merged_files.items():
#         if key not in file2:
#             result[f'- {key}'] = merged_files[key]
#         elif key not in file1:
#             result[f'+ {key}'] = merged_files[key]
#         elif value != file1[key]:
#             result[f'- {key}'] = file1[key]
#             result[f'+ {key}'] = merged_files[key]
#         else:
#             result[key] = value
#
#
#     print(json.dumps(result,indent=2))


output = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''

current_dir = Path(__file__).parent

file1_path = f'{current_dir}/test_files/file1.json'
file2_path = f'{current_dir}/test_files/file2.json'
paths = [file1_path, file2_path]

generate_diff(paths)
assert generate_diff(paths) == output