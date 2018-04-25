# coding=UTF-8
import requests
import json
import random

def get_ip_list(url):
    web_data = requests.get(url)
    text = json.loads(web_data.text)
    ips = text['data']
    ip_list = []
    for i in range(0, len(ips)):
        ip_info = ips[i]
        ip_list.append(ip_info['ip'] + ':' + str(ip_info['port']))
    return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://'+ip)

    proxy_ip = random.choice(proxy_list)

    proxies = {'http': proxy_ip}

    return proxies

def get_ip():
    url = 'http://webapi.http.zhimacangku.com/getip?num=100&type=2&pro=370000&city=0&yys=0&port=1&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions='
    ip_list = get_ip_list(url)
    proxies = get_random_ip(ip_list)
    return proxies

# if __name__ == '__main__':
#     url = 'http://webapi.http.zhimacangku.com/getip?num=10&type=2&pro=&city=0&yys=0&port=1&time=2&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=2&regions='
#     ip_list = get_ip_list(url)
#     proxies = get_random_ip(ip_list)
#     print(proxies)