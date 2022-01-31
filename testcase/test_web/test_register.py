from common.requests_ import vi
import pytest
from midleware.handler import Handler

# 读取用例文件名
cases = Handler.excel.read_data('url')
# 初始化logger
logger = Handler.logger


class TestRegister():

    @pytest.mark.parametrize("case_info", cases)
    def test_register(self, case_info):
        # 补充随机生成注册账号
        data = Handler.random_user().random_phone(case_info['data'])
        # 将data数据 json格式转 转换为字典格式

        # 将生成的测试账号写入数据库

        # 准备测试数据
        params = 'zxsdkpwuser={}&zxsdkpwpwd={}&zxsdkgcode=&zxsdkppname=&zxsdkppcard=&xieyi=on&action=register&checkjsonp=0'.format(
            data['username'], data['password'])
        res = vi(url=case_info['url'],
                 method=case_info['method'],
                 params=params)
        try:
            assert (res['type'], case_info['type'])
            assert (res['data']['username'], data['username'])
            logger.info('测试用例通过')
        except AssertionError as e:
            logger.error('测试用例失败{}'.format(e))
            raise e


if __name__ == '__main__':
    pytest.main()
