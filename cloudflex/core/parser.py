import yaml

def parse_config(file_path='cloudflex.yaml'):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)