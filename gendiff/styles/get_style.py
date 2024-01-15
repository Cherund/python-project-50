from gendiff.styles.stylish import to_stylish
from gendiff.styles.plain_style import to_plain
from gendiff.styles.json_style import to_json


def style_dict(data, style):
    if style == 'plain':
        return to_plain(data)

    if style == 'json':
        return to_json(data)

    if style == 'stylish':
        return to_stylish(data)

    raise ValueError(f'Unknown style: {style}')
