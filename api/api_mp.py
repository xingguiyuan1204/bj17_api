import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()
class ApiMp:
    #初始化
    def __init__(self):
        #定义登录url
        self.url_mp_login = api.HOST + "/mp/v1_0/authorizations"
        #定义发布文章url
        self.url_mp_aritcle = api.HOST + "/mp/v1_0/articles"

    #登录 接口封装
    def api_mp_login(self,mobile,code):

        data = {"mobile": mobile,"code": code}
        log.info("正在调用自媒体登录接口，登录数据：{} headers:{}".format(data, api.headers))
        return requests.post(url=self.url_mp_login,json=data,headers=api.headers)

    # 发布文章 接口封装
    def api_mp_article(self, title, content,channel_id):
        data = {"title":title,"content":content,"channel_id":channel_id,"cover":{"type":0,"images":[]}}
        log.info("正在调用自媒体发布文章，发布数据为：{} 请求头为：{}".format(data, api.headers))
        return requests.post(url=self.url_mp_aritcle, json=data, headers=api.headers)