#/usr/bin/env python
#coding=utf8
import json
import http.client #修改引用的模块
import hashlib #修改引用的模块
from urllib import parse
import random

# 百度开发者api自己去申请

appid = "" #你的appid
secretKey = "" #你的密钥

def bdtrans(word, fromLang, toLang):
    httpClient = None
    myurl = "/api/trans/vip/translate"
    q = word
    salt = random.randint(32768, 65536)
    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl+"?appid="+appid+"&q="+parse.quote(q)+"&from="+fromLang+"&to="+toLang+"&salt="+str(salt)+"&sign="+sign
    try:
        httpClient = http.client.HTTPConnection("api.fanyi.baidu.com")
        httpClient.request("GET", myurl)
        response = httpClient.getresponse()
        #转码
        html = response.read().decode("utf-8")
        html = json.loads(html)
        dst = html["trans_result"][0]["dst"]
        return dst
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
# 原文链接：https://blog.csdn.net/weixin_39610759/article/details/111528864

if __name__ == '__main__':
    print(bdtrans('apple',"auto","zh"))
