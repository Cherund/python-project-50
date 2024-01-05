import json
import yaml


def parse(data, extension):
    if extension == '.json':
        return json.load(data)
    else:
        return yaml.safe_load(data)
