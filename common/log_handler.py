import logging
from common import yaml_handler
from config import config_path
import os

# 获取config配置文件路径
configyl_path = os.path.join(config_path.CONFIG_PATH, 'config.yaml')
# 获取log配置信息
config = yaml_handler.read_yaml(configyl_path)["log"]


class Logger_Handler(logging.Logger):
    def __init__(self,
                 name='root',
                 logger_level='DEBUG',
                 stream_level='INFO',
                 file_level='INFO',
                 file=None,
                 fmt_m='%(asctime)s -【%(filename)s[line:%(lineno)d]】 %(levelname)s %(message)s'
                 ):
        # 初始化父类 得到的self 就是logger本身 收集器
        super().__init__(name, logger_level)
        # 设置收集级别
        self.setLevel(logger_level)
        # 获取日志输出处理器
        str_handler = logging.StreamHandler()
        # 设置控制台输出处理器级别
        str_handler.setLevel(stream_level)
        # 设置日志格式
        fmt = logging.Formatter(fmt_m)
        # 将日志格式添加到处理器
        str_handler.setFormatter(fmt)
        # 将输出处理器添加到收集器里
        self.addHandler(str_handler)
        # 如果file有传入的文件路径，那么就创建文件输出处理器
        if file:
            # 文件输出处理器
            file_handler = logging.FileHandler(file)
            # 设置文件处理器级别
            file_handler.setLevel(file_level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)


if __name__ == '__main__':
    lg = Logger_Handler()
    lg.info('wu')
