import requests
import json

def weather_city(city):
    #和风天气免费开发api https://devapi.qweather.com/v7/weather/now?location=101010100&key=你的KEY
    # 单个插件测试请将API_KEY.json复制到api目录下
    with open("API_KEY.json",'r') as load_f:
        load_dict = json.load(load_f)
        key = load_dict["WEATHER_KEY"]
    """查询城市id"""
    data_id = requests.get("https://geoapi.qweather.com/v2/city/lookup?location={}&key={}".format(city, key))
    content_id = json.loads(data_id.text)
    """城市id"""
    id = content_id['location'][0]["id"]
    """城市名字"""
    name = content_id['location'][0]["name"]
    """以id查询城市天气"""
    data_we = requests.get("https://devapi.qweather.com/v7/weather/now?location={}&key={}".format(id, key))
    content_we = json.loads(data_we.text)
    """实时温度"""
    temp = content_we["now"]["temp"]
    """体感温度"""
    feelsLike = content_we["now"]["feelsLike"]
    """天气"""
    text = content_we["now"]["text"]
    """风向"""
    windDir = content_we["now"]["windDir"]
    """风级数"""
    windScale = content_we["now"]["windScale"]
    """相对湿度"""
    humidity = content_we["now"]["humidity"]
    """能见度"""
    vis = content_we["now"]["vis"]
    """云量"""
    cloud = content_we["now"]["cloud"]
    """降水量"""
    precip = content_we["now"]["precip"]
    """更新时间"""
    time_con = content_we['updateTime']
    date = time_con[0:10]
    time = time_con[11:16]
    """汇总"""
    sum_str = '今天{}天气为{}\n{}{}级\n气温{}度\n体感温度{}度\n相对湿度{}\n可见度{}\n降水量{}\n更新时间{} {}'.format(name, text, windDir, windScale, temp, feelsLike, humidity, vis, precip, date, time)
    return sum_str

if __name__ == '__main__':
    city = '上海'
    print(weather_city(city))
