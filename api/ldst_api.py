import requests
import json

def setu_api(r18):
    # 单个插件测试请将API_KEY.json复制到api目录下
    # 0为非 R18，1为 R18，2为混合
    with open("API_KEY.json",'r') as load_f:
        load_dict = json.load(load_f)
        key = load_dict["LDST_API_KEY"]
    json_con = requests.get(f"https://api.lolicon.app/setu/?apikey={key}&r18={r18}")
    content_st_info = json.loads(json_con.text)
    # 解析
    pid = content_st_info["data"][0]["pid"]
    uid = content_st_info["data"][0]["uid"]
    title = content_st_info["data"][0]["title"]
    author = content_st_info["data"][0]["author"]
    url = content_st_info["data"][0]["url"]
    return [url, title, author, uid, pid]


if __name__ == '__main__':
    print(setu_api(0))
