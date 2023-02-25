import os
import json
from constants import default_config


def exists(path):
    return os.path.isfile(path)


def get_or_create(path):
    if not exists(path):
        create(path, json.dumps(default_config, indent=4))
        return None
    else:
        file = open(path, 'r')
        result = json.load(file)
        file.close()
        return result


def create(path, content):
    file = open(path, "w+")
    file.write(content)
    file.close()
