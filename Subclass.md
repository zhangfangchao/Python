# 利用Requests+Xpath 爬取百姓网频道

> 爬虫的基本流程
简单来说，我们向服务器发送请求后，会得到返回的页面，通过解析页面之后，我们可以抽取我们想要的那部分信息，并存储在指定的文档或数据库中。这样，我们想要的信息就被我们 “爬” 下来啦~

1. 请求并下载百姓网领养宠物页面
2. 解析并定位想要的数据
3. 保存想要的数据

 ```python
 #-*- coding: utf-8 -*
from lxml import etree
import requests
import time
from retrying import retry

headers = {
            "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",

            "Referer": "https://www.baidu.com/link?url=Uihi10khyVB8YVd1zPmjuvRANJ_G98qcaAqnBMOT1KNG84wYcAMGClyWVJDttD5KvYp2pCafPMW28XjbJ1o-8a&wd=&eqid=f2752cb20003b423000000035ad706b5"
             }
with open('/Users/dayu_ui/Desktop/大客户登录/animal.csv','w',encoding='utf-8''\r\n') as f:
    for a in range(1,6):
        url = 'http://beijing.baixing.com/m/chongwulingyang/m33633/?page={}'.format(a)
        data = requests.get(url,headers=headers).text

        s=etree.HTML(data)
        file = s.xpath('//html/body/article/main/section/ul/li/a')
        time.sleep(2)


        for div in file:
            title = div.xpath('./div[2]/h3/text()')[0]
            showtime = div.xpath('./div[2]/p/span/strong/time/text()')[0]
            addr = div.xpath('./div[2]/div/span/text()')[0]
            url1 = div.xpath('./@href')
            img = div.xpath('./div/img/@*')

            print(title,showtime,addr,url1)


            f.write("{},{},{},{}\n".format(title,showtime,addr,url1))
```
