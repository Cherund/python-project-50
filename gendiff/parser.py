import json
import yaml


def parse(data, extension):
    match extension:
        case 'json':
            return json.load(data)
        case 'yml':
            return yaml.safe_load(data)

    ValueError(f'Unsupported extension: {extension}')
