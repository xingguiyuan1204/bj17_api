import api
from tools.get_log import GetLog
log = GetLog.get_logger()


class Tools:
    # 提取token
    @classmethod
    def get_token(cls,r):
        # 提取token
        token = r.json().get("data").get("token")
        log.info("正在提取token:{}".format(token))
        # 将token追加到api.headers
        api.headers["Authorization"] = "Bearer " + token
        log.info("合并的api.headers为{}".format(api.headers))

    # 断言

    @classmethod
    def assert_common(cls,r,message="OK",code=201):
        try:
            #断言响应信息
            assert message == r.json().get("message")
            #断言状态码
            assert code == r.status_code
        except Exception as e:
            log.error(e)
            raise