import os
import time
from pathlib import Path

from config import config_path

reports_filename = 'report_{}.txt'.format(time.strftime('%Y/%m/%d %H:%M:%S'))
# 测试报告路径
reports_path = os.path.join(config_path.REPORTS_PATH, reports_filename)
print(reports_path)
# print(Path(__file__).parent.parent.joinpath(reports_filename))
print(Path.cwd().parent.joinpath('reports').joinpath(reports_filename))
