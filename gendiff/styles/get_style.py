from gendiff.styles.stylish import to_stylish
from gendiff.styles.plain_style import to_plain
from gendiff.styles.json_style import to_json


def style_dict(dic, style):
    if style == 'plain':
        return to_plain(dic)

    if style == 'json':
        return to_json(dic)

    return to_stylish(dic)
