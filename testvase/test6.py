import json
import requests

class Test_login(object):

    dongman='https://apiv2.vcomic.com/'
    def test_login(self):
        path='wbcomic/account/user_info?_ver=7.8.6&_type=iphone&_mark=1FBEF30E-03A4-4C92-BF34-03973F40363A&_channel=appstore&_debug_=yes'
        url=self.dongman+path
        res=requests.get(url).json()

        assert res['message'] == ok