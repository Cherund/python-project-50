from gendiff.constants import CHANGES_TYPES


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
                case CHANGES_TYPES.REMOVED:
                    result.append(f"Property '{print_path}' was removed")
                case CHANGES_TYPES.ADDED:
                    result.append(f"Property '{print_path}' was added with "
                                  f"value: {checking_value(value['value'])}")
                case CHANGES_TYPES.UPDATED:
                    result.append(f"Property '{print_path}' was updated. "
                                  f"From {checking_value(value['old_value'])} "
                                  f"to {checking_value(value['new_value'])}")
                case CHANGES_TYPES.NESTED:
                    result.extend(_iter_plain(value['value'], print_path))
                case CHANGES_TYPES.UNCHANGED:
                    continue
                case _:
                    raise ValueError(f'Unknown type: {value["type"]}')

        return result

    result_string = '\n'.join(_iter_plain(data))
    return result_string
