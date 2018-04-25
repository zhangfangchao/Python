# coding=UTF-8
import requests
import ip_list1
import ip1
import time

maparas={
    "action":"qaptcha",
    "isgz":"0",
    "projectid":"7114",
    "redirecturl":"",
    "shopid":"83866",
    "token":"5639FD07C641DF3E3133F067083A1D63F44FC365A27E13289BBAC11C5241B3CE"
            }
headers ={"User-Agent":"Mozilla/5.0 (Linux; U; Android 2.3.6; zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger/4.5.255"
          }
url = "http://rz.dukey.cn/ashx/diy.ashx?ac=wx_vote"
num = 0

for i in range(100):
    time.sleep(2)

    proxies = ip_list1.get_ip()
    url = "http://rz.dukey.cn/ashx/diy.ashx?ac=wx_vote"

    r = requests.post(url, data=maparas, headers=headers, proxies=proxies)
    print("get请求获取响应状态码", r.text)

    print(proxies)