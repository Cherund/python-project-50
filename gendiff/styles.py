def to_string(value, indent=2):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'{" " * indent}  '
                         f'{key}: {to_string(val, indent + 4)}\n')
        return f'{{\n{"".join(lines)}{" " * (indent-2)}}}'
    return value


def stylish(dic, indent=2):
    result = []
    for key, value in dic.items():
        if value['type'] == 'removed':
            result.append(f'{" " * indent}- {key}: '
                          f'{to_string(value["value"], indent+4)}')
        elif value['type'] == 'added':
            result.append(f'{" " * indent}+ {key}: '
                          f'{to_string(value["value"], indent+4)}')
        elif value['type'] == 'updated':
            result.append(f'{" " * indent}- {key}: '
                          f'{to_string(value["value1"], indent+4)}')
            result.append(f'{" " * indent}+ {key}: '
                          f'{to_string(value["value2"], indent+4)}')
        elif value['type'] == 'unchanged':
            result.append(f'{" " * indent}  {key}: '
                          f'{to_string(value["value"], indent+4)}')
        elif value['type'] == 'dictionary':
            result.append(f'{" " * indent}  {key}: '
                          f'{stylish(value["value"], indent+4)}')
        else:
            raise ValueError(f'Unknown type: {value["type"]}')

    result_string = '\n'.join(result)
    return f'{{\n{result_string}\n{" " * (indent-2)}}}'


def checking_value(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'

    return f"'{value}'"


def plain(dic, path=[]):
    result = []
    for key, value in dic.items():
        if 'type' in value:
            print_path = '.'.join(path+[key])
            if value['type'] == 'removed':
                result.append(f"Property '{print_path}' was removed")
            elif value['type'] == 'added':
                result.append(f"Property '{print_path}' was added with "
                              f"value: {checking_value(value['value'])}")
            elif value['type'] == 'updated':
                result.append(f"Property '{print_path}' was updated. "
                              f"From {checking_value(value['value1'])} "
                              f"to {checking_value(value['value2'])}")
            elif plain(value):
                result.append(plain(value, path+[key]))

        elif isinstance(value, dict) and plain(value):
            result.append(plain(value, path))

    result_string = '\n'.join(result)
    return result_string
