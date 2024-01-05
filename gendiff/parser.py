import json
import yaml
import os


def parse(data):
    extension = os.path.splitext(data.name)[1]
    if extension == '.json':
        return json.load(data)
    else:
        return yaml.safe_load(data)
