def checking_value(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'

    return f"'{value}'"


def to_plain(data):
    def _iter_plain(data, path=''):
        result = []
        for key, value in data.items():
            print_path = f"{path}.{key}" if path else f'{key}'
            match value['type']:
                case 'removed':
                    result.append(f"Property '{print_path}' was removed")
                case 'added':
                    result.append(f"Property '{print_path}' was added with "
                                  f"value: {checking_value(value['value'])}")
                case 'updated':
                    result.append(f"Property '{print_path}' was updated. "
                                  f"From {checking_value(value['old_value'])} "
                                  f"to {checking_value(value['new_value'])}")
                case 'nested':
                    result.extend(_iter_plain(value['value'], print_path))
                case 'unchanged':
                    continue
                case _:
                    raise ValueError(f'Unknown type: {value["type"]}')

        return result

    result_string = '\n'.join(_iter_plain(data))
    return result_string
