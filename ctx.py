# -*- coding: utf-8 -*-

from ruamel.yaml import YAML
from pymongo import MongoClient


def yaml_loader(filepath):
    with open(filepath, encoding='utf8') as f:
        yaml = YAML()
        data = yaml.load(f)
        return data


config = yaml_loader('./conf.yaml')

# 数据库前缀
DB_PREFIX = config.get("sys").get("db_prefix")


mdb = MongoClient(**config.get("sys").get("mongoDb"))


def get_db(module):

    return mdb[DB_PREFIX + module]


# 配置数据库
config_mdb = get_db("config")


tide_base_mdb = get_db("tide")
tide_out_mdb = get_db("out")
