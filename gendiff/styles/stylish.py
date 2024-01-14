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


def to_stylish(dic, indent=2):
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
                          f'{to_stylish(value["value"], indent+4)}')
        else:
            raise ValueError(f'Unknown type: {value["type"]}')

    result_string = '\n'.join(result)
    return f'{{\n{result_string}\n{" " * (indent-2)}}}'