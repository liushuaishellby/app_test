import json

import pytest
from midleware import handler
from common.requests_ import vi

Handler = handler.Handler()
cases = Handler.excel.read_data('app_login')
logger = Handler.logger

class TestAppLogin(object):

    @pytest.mark.app_login
    @pytest.mark.parametrize("cases", cases)
    def test_app_login(self, cases):
        data = json.dumps(cases['data'])
        headers = eval(cases['headers'])
        expt = eval(cases['expected'])
        rsq = vi(url=cases['url'], method=cases['method'], data=data, headers=headers)
        try:
            assert (expt['code'] == rsq['code'])
            assert (expt['msg'] == rsq['msg'])
            logger.info("测试用例通过")
        except AssertionError as e:
            logger.error("测试失败{}".format(e))
            raise e

    # @pytest.mark.app_login1
    # @pytest.mark.parametrize("cases_info", cases)
    # def test_app_login1(self, cases_info):
    #     data = json.dumps(cases_info['data'])
    #     headers = eval(cases_info['headers'])
    #     print(headers)
    #     rsq = vi(url=cases_info['url'], method=cases_info['method'], data=data, headers=headers)
    #     print(rsq)


