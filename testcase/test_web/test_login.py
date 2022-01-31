from midleware import handler
import pytest

Handler = handler.Handler()
# 获取表格数据路径\获取用例表格数据
cases = Handler.excel.read_data('login')
# 初始化log
log = Handler.logger


class TestLogin:
    @pytest.mark.add
    # 参数化
    @pytest.mark.parametrize("case_info", cases)
    def test_add(self, case_info):
        data = eval(case_info['data'])
        print(data['username'], data['password'], case_info['title'])
        log.info("测试通过")


if __name__ == '__main__':
    pytest.main()
