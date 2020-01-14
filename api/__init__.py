
from tools.read_txt import read_txt
#定义公共的URL
HOST = "http://ttapi.research.itcast.cn"
# 信息头
headers = {"Content-Type": "application/json"}
# 文章id
article_id = None
# 文章标题
title = read_txt("mp_article.txt")[0][0]
# 频道名
channel = read_txt("mp_article.txt")[0][3]
# 频道id
channel_id = read_txt("mp_article.txt")[0][2]