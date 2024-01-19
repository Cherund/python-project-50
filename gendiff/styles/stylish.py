from gendiff.styles.constants import TYPES, INDENT


def build_indent(depth):
    return INDENT[:-2] + INDENT * depth


def format_data(data, depth):
    string_data = '\n'.join(data)
    last_indent = build_indent(depth)[:-2]
    return f'{string_data}\n{last_indent}'


def create_braces(formatted_data):
    return f'{{\n{formatted_data}}}'


def to_string(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        lines = []
        for key, val in value.items():
            lines.append(f'{build_indent(depth)}  '
                         f'{key}: {to_string(val, depth + 1)}')
        lines_string = format_data(lines, depth)
        return create_braces(lines_string)
    return value


def to_stylish(data, depth=0):
    result = []
    for key, value in data.items():
        match value['type']:
            case TYPES.REMOVED:
                result.append(f'{build_indent(depth)}- {key}: '
                              f'{to_string(value["value"], depth + 1)}')
            case TYPES.ADDED:
                result.append(f'{build_indent(depth)}+ {key}: '
                              f'{to_string(value["value"], depth + 1)}')
            case TYPES.UPDATED:
                result.append(f'{build_indent(depth)}- {key}: '
                              f'{to_string(value["old_value"], depth + 1)}')
                result.append(f'{build_indent(depth)}+ {key}: '
                              f'{to_string(value["new_value"], depth + 1)}')
            case TYPES.UNCHANGED:
                result.append(f'{build_indent(depth)}  {key}: '
                              f'{to_string(value["value"], depth + 1)}')
            case TYPES.NESTED:
                result.append(f'{build_indent(depth)}  {key}: '
                              f'{to_stylish(value["value"], depth + 1)}')
            case _:
                raise ValueError(f'Unknown type: {value["type"]}')

    result_string = format_data(result, depth)
    return create_braces(result_string)
