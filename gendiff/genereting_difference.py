from gendiff.parser import parse


def to_string(value):
    if isinstance(value, bool):
        return str(value).lower()
    return value


def get_file_data(file_path):
    with open(file_path) as file:
        return parse(file)


def generate_diff(file1_path, file2_path):
    file1 = get_file_data(file1_path)
    file2 = get_file_data(file2_path)
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
