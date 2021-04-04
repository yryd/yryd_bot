import requests
from lxml import etree
from urllib import parse
import random

"""双生世界人物卡池（普池）返回4个稀有度卡池，爬取b站wiki"""
def request_draw():
    headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36"
    }
    url = 'https://wiki.biligame.com/sssj/%E5%8D%A1%E7%89%8C%E5%9B%BE%E9%89%B4'
    responds = requests.get(url, headers=headers)
    content = responds.content.decode()
    html =etree.HTML(content)
    # 卡片名字
    name = html.xpath('//div[@data-param7="普池补给"]//div[@class="kptj-blank"]/a/@title')
    # 总卡池分成稀有度卡池rank_4 - 1为金卡池到白卡池
    rank = html.xpath('//div[@data-param7="普池补给"]/@data-param1')
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
    rank_4,rank_3,rank_2,rank_1 = request_draw()
    print(rank_4,rank_3,rank_2,rank_1)

# https://wiki.biligame.com/sssj/%E5%86%AC%E8%A3%85%C2%B7%E4%BC%8A%E7%8F%82%E4%B8%9D
