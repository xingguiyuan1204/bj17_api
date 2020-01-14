from api.api_app import ApiApp
from tools.tools import Tools

class TestAPP():

    def setup_class(self):
        self.app = ApiApp()

    def test01_app_login(self):
        r = self.app.api_app_login()
        # 提取token
        Tools.get_token(r)
        # 断言
        Tools.assert_common(r)

    def test02_app_search(self):
        r = self.app.api_app_search()
        # 断言
        Tools.assert_common(r,code=200)






