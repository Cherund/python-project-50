from gendiff.styles.stylish import to_stylish
from gendiff.styles.plain import to_plain
from gendiff.styles.json import to_json
from gendiff.styles.constants import FORMATS


def format_diff(data, style):
    match style:
        case FORMATS.PLAIN:
            return to_plain(data)

        case FORMATS.JSON:
            return to_json(data)

        case FORMATS.STYLISH:
            return to_stylish(data)

        case _:
            raise ValueError(f'Unknown style: {style},'
                             f' please choose from [{", ".join(FORMATS)}]')
