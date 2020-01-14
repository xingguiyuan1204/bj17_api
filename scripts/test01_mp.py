
import pytest
import api

from api.api_mp import ApiMp
from tools.read_txt import read_txt
from tools.tools import Tools


class TestMp():

    def setup_class(self):
        self.mp = ApiMp()

    @pytest.mark.parametrize("mobile,code", read_txt("mp_login.txt"))
    def test01_mp_login(self,mobile,code):
        r = self.mp.api_mp_login(mobile,code)
        # 提取token
        Tools.get_token(r)
        # 断言
        Tools.assert_common(r)

    @pytest.mark.parametrize("title,content,channel_id,channel", read_txt("mp_article.txt"))
    def test02_mp_article(self,title,content,channel_id,channel):
        r = self.mp.api_mp_article(title,content,channel_id)
        # 提取文章id
        api.article_id = r.json().get("data").get("id")
        # 断言
        Tools.assert_common(r)



