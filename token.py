import yaml


def fetch_token(config_path='config.yaml'):
    with open(config_path) as configfile:
        config = yaml.load(configfile.read())

    return config['token']

