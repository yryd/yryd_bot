import requests
from lxml import etree
from urllib import parse
import random

"""双生世界武器池（普池）返回4个稀有度卡池，爬取b站wiki"""
def request_drawweapon():
    headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36"
    }
    url = 'https://wiki.biligame.com/sssj/%E6%AD%A6%E5%99%A8%E5%9B%BE%E9%89%B4'
    responds = requests.get(url, headers=headers)
    content = responds.content.decode()
    html =etree.HTML(content)
    # 武器名
    name = html.xpath('//tr[@data-param3="普池补给"]//div[@class="floatnone"]/a/@title')
    # 总卡池分成稀有度卡池rank_4 - 1为金卡池到白卡池
    rank = html.xpath('//tr[@data-param3="普池补给"]/@data-param2')
    rank_4 = []
    rank_3 = []
    rank_2 = []
    rank_1 = []
    for i,j in zip(rank, name):
        if i == '4':
            rank_4.append(j)
        if i == '3':
            rank_3.append(j)
        if i == '2':
            rank_2.append(j)
        if i == '1':
            rank_1.append(j)
    return (rank_4,rank_3,rank_2,rank_1)

if __name__ == '__main__':
    rank_4,rank_3,rank_2,rank_1 = request_drawweapon()
    print(rank_4,rank_3,rank_2,rank_1)

# https://wiki.biligame.com/sssj/%E6%AD%A6%E5%99%A8%E5%9B%BE%E9%89%B4
