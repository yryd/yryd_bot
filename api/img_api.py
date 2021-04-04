import requests
import json

"""免费图片api，随时失效"""
def img_get_1():
    #小歪 https://api.ixiaowai.cn/  动漫图
    url = 'https://api.ixiaowai.cn/api/api.php?return=json'
    json_con = requests.get(url, verify = False)
    decoded_d = json_con.content.decode('utf-8-sig')
    content_st_info = json.loads(decoded_d)
    imgurl = content_st_info["imgurl"]
    return imgurl

def img_get_2():
    #小歪 https://api.ixiaowai.cn/  mc酱
    url = 'https://api.ixiaowai.cn/mcapi/mcapi.php?return=json'
    json_con = requests.get(url, verify = False)
    decoded_d = json_con.content.decode('utf-8-sig')
    content_st_info = json.loads(decoded_d)
    imgurl = content_st_info["imgurl"]
    return imgurl

def img_get_3():
    # https://img.xjh.me/ 图片源
    url = 'https://img.xjh.me/random_img.php?return=json'
    json_con = requests.get(url)
    content_st_info = json.loads(json_con.text)
    imgurl = content_st_info["img"]
    imgurl = 'https:' + imgurl
    return imgurl

def img_get_4():
    # https://acg.toubiec.cn/ 图源
    url = 'https://acg.toubiec.cn/random.php?ret=json'
    json_con = requests.get(url)
    content_st_info = json.loads(json_con.text)
    imgurl = content_st_info[0]["imgurl"]
    return imgurl

def img_get_5():
    # https://api.mtyqx.cn/图源
    url = 'https://api.mtyqx.cn/api/random.php?return=json'
    json_con = requests.get(url)
    content_st_info = json.loads(json_con.text)
    imgurl = content_st_info["imgurl"]
    return imgurl

def img_get_6():
    # https://api.mtyqx.cn/ 图源
    url = 'https://api.mtyqx.cn/tapi/random.php?return=json'
    json_con = requests.get(url)
    content_st_info = json.loads(json_con.text)
    imgurl = content_st_info["imgurl"]
    return imgurl

def star_num(num):
    inum = int(num)
    if inum == 1:
        url = img_get_1()
        return url
    elif inum == 2:
        url = img_get_2()
        return url
    elif inum == 3:
        url = img_get_3()
        return url
    elif inum == 4:
        url = img_get_4()
        return url
    elif inum == 5:
        url = img_get_5()
        return url
    elif inum == 6:
        url = img_get_6()
        return url
    else:
        return False
if __name__ == '__main__':
    print(star_num(1))
