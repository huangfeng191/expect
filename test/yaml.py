from ruamel.yaml import YAML


def yaml_loader(filepath):
   with open(filepath) as f:
      yaml=YAML()
      data=yaml.load(f)
      return data 

config=yaml_loader('./conf.yaml')



