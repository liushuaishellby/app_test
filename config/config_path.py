"""
获取路径
"""

import os
from pathlib import Path

# 获取当前路径
CONFIG_PATH = Path(__file__).parent

# 获取项目路径
ROOT_PATH = CONFIG_PATH.parent

# 获取测试用例路径
TEST_PATH = ROOT_PATH.joinpath('testcase')

# 获取测试测报路径
REPORTS_PATH = ROOT_PATH.joinpath('reports')

# 获取data测试数据路径
DATA_PATH = ROOT_PATH.joinpath('data')

# 获取logs日志路径
LOG_PATH = ROOT_PATH.joinpath('logs')

# 获取common路径
COMMON_PATH = ROOT_PATH.joinpath('common')

# 获取libs路径
LIBS_PATH = ROOT_PATH.joinpath('libs')

if __name__ == '__main__':
    print(TEST_PATH)
