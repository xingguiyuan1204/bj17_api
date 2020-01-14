import time

import api
import requests

from tools.read_txt import read_txt


class ApiApp:
    # 初始化
    def __init__(self):
        self.url_app_login = api.HOST + "/app/v1_0/authorizations"

        self.url_app_search = api.HOST + "/app/v1_1/articles"

    # 登录app接口
    def api_app_login(self):
        login_data = read_txt("mp_login.txt")[0]
        data = {"mobile": login_data[0], "code": login_data[1]}
        return requests.post(url=self.url_app_login, json=data, headers=api.headers)

    # 查询频道接口
    def api_app_search(self):
        data = {"channel_id": api.channel_id, "timestamp": int(time.time()), "with_top": 1}  # with_top 1表示包含指定  0不包含
        return requests.get(url=self.url_app_search, params=data, headers=api.headers)
