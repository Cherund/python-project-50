from gendiff.styles.stylish import to_stylish
from gendiff.styles.plain_style import to_plain
from gendiff.styles.json_style import to_json


def style_dict(data, style):
    if style == 'plain':
        return to_plain(data)

    elif style == 'json':
        return to_json(data)

    elif style == 'stylish':
        return to_stylish(data)

    else:
        raise ValueError(f'Unknown style: {style}')
