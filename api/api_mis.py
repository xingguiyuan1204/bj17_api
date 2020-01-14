import api
import requests

from tools.get_log import GetLog

log = GetLog


class ApiMis():

    def __init__(self):
        # 登录的url
        self.url_mis_login = api.HOST + "/mis/v1_0/authorizations"

        # 查询的url
        self.url_mis_search = api.HOST + "/mis/v1_0/articles"

        # 审核的url
        self.url_mis_audit = api.HOST + "/mis/v1_0/articles"

    # 后台登录接口
    def api_mis_login(self, account, password):
        data = {"account": account, "password": password}
        return requests.post(url=self.url_mis_login, json=data, headers=api.headers)

    # 后台查询接口
    def api_mis_search(self):
        data = {"title": api.title, "channel": api.channel}
        return requests.get(url=self.url_mis_search, params=data, headers=api.headers)

    # 后台审核接口
    def api_mis_audit(self):
        data = {"article_ids": api.article_id, "status": 2}  # 2表示审核通过
        return requests.put(url=self.url_mis_audit, json=data, headers=api.headers)
