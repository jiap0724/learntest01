import requests

import pytest
class test_api(object):

    dongman='https://apiv2.vcomic.com/'
    def test_login(self):
        path1='wbcomic/account/user_info?_ver=7.8.6&_type=iphone&_mark=1FBEF30E-03A4-4C92-BF34-03973F40363A&_channel=appstore&_debug_=yes'
        url1=self.dongman+path1
        result=requests.get(url1).json()

        assert result['user_id'] == 0