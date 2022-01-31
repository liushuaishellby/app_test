import os
from config import config_path
from common import yaml_handler, exel_handler, log_handler
from common.mysql_hangdler import GetMysql
import random
import json


class MysqlHandlerMid(GetMysql):
    def __init__(self):
        super().__init__(user='root',
                         pwd='123456',
                         host='localhost',
                         port=3306
                         )


class RandomNumber:
    def random_phone(self, case):
        """
        生成随机数，如果随机数已经在数据库就继续 从新继续生成
        """
        # 判断 #phone 是否 在case的数据里面， 如果没有就直接转换为字典返回
        if '#phone' in case:
            # 永远循环 直到随机生成的数据在数据库里没有为止
            while True:
                phone = random.choice(['a', 'c', 'y', 'p']) + random.choice(['a', 'b', 'c', 'e'])
                for i in range(9):
                    phone += str(random.randint(0, 9))
                case_info = json.loads(case.replace('#phone', phone))
                sql_code = "select * from my_databases.people where username = '{}'".format(case_info['username'])
                query = Handler.db().select_mysql(sql_code)
                if not query:
                    return case_info
        return json.loads(case)


class Handler:
    """
    初始化所有关于数据的方法，方便重复使用，节省代码
    """
    # 获取配置项信息
    conf = config_path

    # 获取yaml信息
    yaml = yaml_handler.read_yaml(conf.CONFIG_PATH.joinpath('config.yaml'))

    # 初始化excel
    __excel_path = conf.DATA_PATH
    __excel_file = yaml['excel']['file']
    excel = exel_handler.ExcelHandler(__excel_path.joinpath(__excel_file))

    # 初始化logger
    logger = log_handler.Logger_Handler(
        name='root',
        logger_level=yaml['log']['logger_level'],
        stream_level=yaml['log']['stream_level'],
        file_level=yaml['log']['file_level'],
        file=os.path.join(config_path.LOG_PATH, yaml['log']['file']))
    db = MysqlHandlerMid
    random_user = RandomNumber


def replace_data(data):
    # 注意传入的data必须是个字符串
    import re
    # 创建匹配表达式
    part = r"#(.*?)#"
    # 使用while循环 直到字符串没有#(.*?)#的字符为止。
    while re.search(part, data):
        # 获取key 目的是查询要替换的字符 是哪个字段
        key = re.search(part, data).group(1)
        print(key)
        # 创建value 用于使用类的属性 来获取要替换的数据
        # value = getattr(类名, key, '')
        # 开始替换    因为这个类里面没phone这个属性 所以这里他会替换成空。
        # data = re.sub(part, value, data, count=1)
        return data


if __name__ == '__main__':
    case_info = '{"username": "#phone", "password": "abc123456"}'
    data = Handler.random_user().random_phone(case_info)
    print(case_info)
    print(data)
