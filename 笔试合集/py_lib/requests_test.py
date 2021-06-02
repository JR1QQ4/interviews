#!/usr/bin/python
# -*- coding:utf-8 -*-
import requests

# import requests
# data = {
#     "method": "get",
#     "url": "https://www.juhe.cn/docs/api/id/63",
#     "params": {
#         "key": "57d46b7258fc47e14290c33537f23d36",
#         "data": "4/13"
#     },
#     "headers": {}
# }
# res = requests.request(**data)
# print(res.content.decode('utf-8'))
# res.encoding = "utf-8"
# with open('a.html', 'w', encoding='utf-8') as f:
#     f.write(res.text)

# import json
# dl = {
#     "a": None,
#     "b": False,
#     "c": True,
#     "d": "BAB2",
#     "e": ["1", 12],
#     "f": {"ln": 90},
#     "g": {"h": 1, "i": "11", "j": True}
# }
# print(type(dl))
# dl_js = json.dumps(dl)
# print(type(dl_js))
# print(dl_js)
# js_dl = json.loads(dl_js)
# print(type(js_dl))
# print(js_dl)

# import requests
# url = "http://www.cnblogs.com/yoyoketang/"
# r = requests.get(url)
# print(r.text)  # 这个为什么不报错
# print(type(r.text))
# print(r.json())

from lxml import etree
res = requests.get("http://www.baidu.com")
html_str = res.content.decode("utf-8")
demo = etree.HTML(html_str)
nodes = demo.xpath('//*[@id="cp"]')
print(nodes[0].text)  # ©2017 Baidu
print(nodes[0].xpath("string(.)"))  # ©2017 Baidu 使用百度前必读  意见反馈 京ICP证030173号



