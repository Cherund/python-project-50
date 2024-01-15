def checking_value(value):
    if isinstance(value, (bool, int)):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'

    return f"'{value}'"


def to_plain(data, path=[]):
    result = []
    for key, value in data.items():
        if 'type' in value:
            print_path = '.'.join(path + [key])
            if value['type'] == 'removed':
                result.append(f"Property '{print_path}' was removed")
            elif value['type'] == 'added':
                result.append(f"Property '{print_path}' was added with "
                              f"value: {checking_value(value['value'])}")
            elif value['type'] == 'updated':
                result.append(f"Property '{print_path}' was updated. "
                              f"From {checking_value(value['value1'])} "
                              f"to {checking_value(value['value2'])}")
            else:
                if key == 'value':
                    appending_value = to_plain(value, path)
                else:
                    appending_value = to_plain(value, path + [key])

                if appending_value:
                    result.append(appending_value)

        elif isinstance(value, dict):
            appending_value = to_plain(value, path)
            if appending_value:
                result.append(to_plain(value, path))

    result_string = '\n'.join(result)
    return result_string
