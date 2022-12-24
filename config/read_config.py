import os
from configparser import ConfigParser
from configobj import ConfigObj

# 获取当下文件夹的目录
rootPath = os.path.abspath(os.path.split(os.path.abspath(os.path.realpath(__file__)))[0] + "/../")
config_path = rootPath + '/config/base_config.ini'
# 初始化ConfigParser方法，并读取配置文件
config = ConfigParser()
config.read(config_path, encoding='utf-8')


class ReadConfig:
    @staticmethod
    def get_data(key, value):
        key_value = config.get(key, value)
        return key_value
