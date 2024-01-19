from collections import namedtuple


_FORMAT_VALUES = ('stylish', 'plain', 'json')
FORMATS = namedtuple('FormatChoices',
                     map(str.upper, _FORMAT_VALUES))(*_FORMAT_VALUES)

_TYPE_VALUES = ('removed', 'added', 'nested', 'updated', 'unchanged')
CHANGES_TYPES = namedtuple('FormatTypes',
                           map(str.upper, _TYPE_VALUES))(*_TYPE_VALUES)

INDENT = '    '
