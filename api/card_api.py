import requests
from lxml import etree
from urllib import parse

"""根据卡牌名爬取双生wiki上的卡牌图片，返回图片url与图片名"""
def request_sssj_card(char):
    headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Mobile Safari/537.36"
    }
    url = f'https://wiki.biligame.com/sssj/{char}'
    responds = requests.get(url, headers=headers)
    content = responds.content.decode()
    html =etree.HTML(content)
    """Xpath解读数据，可在浏览器中安装插件，数据可能经过加密，响应200返回数组为空"""
    name = html.xpath('//div[@class="floatnone"]/a/img/@alt')
    src = html.xpath('//div[@class="floatnone"]/a/img/@src')
    return name[0], src[0]

if __name__ == '__main__':
    char = '水着·伊珂丝'
    name, src = request_sssj_card(char)
    print(name + ', ' + src)
# https://wiki.biligame.com/sssj/%E5%86%AC%E8%A3%85%C2%B7%E4%BC%8A%E7%8F%82%E4%B8%9D
