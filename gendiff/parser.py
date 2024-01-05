import json, os, yaml


def parse(data):
    extension = os.path.splitext(data.name)[1]
    if extension == '.json':
        return json.load(data)
    else:
        return yaml.safe_load(data)