import yaml


def read_yaml(file):
    with open(file, "r", encoding='UTF-8') as f:
        return yaml.load(f, Loader=yaml.SafeLoader)
