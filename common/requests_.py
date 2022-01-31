from _ast import Expression
import requests
import logging


def vi(url,
       method='get',
       data=None,
       json=None,
       params=None,
       headers=None,
       **kwargs):
    res = requests.request(method, url, data=data, json=json, params=params, headers=headers)
    try:
        return res.json()
    except Exception as e:
        logging.error('不支持此类型数据{}'.format(e))
        return None


class Requests_handers:
    def __init__(self,
                 url,
                 method='get',
                 data=None,
                 json=None,
                 params=None,
                 headers=None,
                 ):
        try:
            self.quests = requests.request(method, url,
                                           data=data,
                                           json=json,
                                           params=params,
                                           headers=headers).json()
        except Exception as e:
            logging.error('不支持此类型数据{}'.format(e))
            self.quests = None


if __name__ == '__main__':
    url = 'http://120.78.128.25:8766/futureloan'
    rs = Requests_handers(url)
    print(rs.quests)
