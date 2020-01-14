
from api.api_mis import ApiMis
from tools.tools import Tools


class TestMis():

    def setup_class(self):
        self.mis = ApiMis()

    def test01_mis_login(self,account="testid",pwd="testpwd123"):
        r = self.mis.api_mis_login(account,pwd)
        # 提取token
        Tools.get_token(r)
        # 断言
        Tools.assert_common(r)

    def test02_mis_search(self):
        r = self.mis.api_mis_search()
        # 断言
        Tools.assert_common(r,code=200)

    def test03_mis_audit(self):
        r = self.mis.api_mis_audit()
        # 断言
        Tools.assert_common(r)




