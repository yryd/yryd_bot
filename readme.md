# 「二·次·元」酱QQ机器人


 基于 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp)，使用[NoneBot](https://docs.nonebot.dev/guide/)框架 
<p align="center">
  <a href="#">
    <img src="https://img.shields.io/badge/python-v3.7%2B-green" alt="license">
  </a>
  <a href=https://docs.nonebot.dev/guide/">
    <img src="https://img.shields.io/badge/OneBot-v11-blue?style=flat&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEAAAABABAMAAABYR2ztAAAAIVBMVEUAAAAAAAADAwMHBwceHh4UFBQNDQ0ZGRkoKCgvLy8iIiLWSdWYAAAAAXRSTlMAQObYZgAAAQVJREFUSMftlM0RgjAQhV+0ATYK6i1Xb+iMd0qgBEqgBEuwBOxU2QDKsjvojQPvkJ/ZL5sXkgWrFirK4MibYUdE3OR2nEpuKz1/q8CdNxNQgthZCXYVLjyoDQftaKuniHHWRnPh2GCUetR2/9HsMAXyUT4/3UHwtQT2AggSCGKeSAsFnxBIOuAggdh3AKTL7pDuCyABcMb0aQP7aM4AnAbc/wHwA5D2wDHTTe56gIIOUA/4YYV2e1sg713PXdZJAuncdZMAGkAukU9OAn40O849+0ornPwT93rphWF0mgAbauUrEOthlX8Zu7P5A6kZyKCJy75hhw1Mgr9RAUvX7A3csGqZegEdniCx30c3agAAAABJRU5ErkJggg==" alt="cqhttp">
  </a>
  <a href="https://github.com/Yang9999999/Go-CQHTTP-YesBot/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/LICENSE-MIT-orange" alt="action">
  </a>
</p>
采用python编写的QQ机器人插件，可用于简易跑团、双生视界抽卡、pixiv图片下载。
采用标准接口易于拓展

## 目前拥有的功能

- 1.跑团类（包括简易车卡coc/dnd、掷骰子）
- 2.图片类（包括随机图片、壁纸(6个图库)）
- 3.杂类（包括翻译、今日人品等）
- 4.双生视界（包括抽卡、抽武器、卡面获取）
- 5.隐藏命令（p站pid搜图、目标语言循环翻译、p站标签搜图）

## 配置

配置_1在API_KEY.json中

```json
{
  "LDST_API_KEY":"",
  "WEATHER_KEY":""
}
```
分别为 

- 色图api的key
- 和风天气api的key


配置_2在config.py中
```py
SUPERUSERS = {264xxxxxx} #填写本人QQ
COMMAND_START = {'/', '!', '／', '！', '.', '。'} #命令接受的开头
HOST = '127.0.0.1'
PORT = 8080
NICKNAME = {'阿sir', '啊sir'} #呼叫机器人方法
SESSION_RUNNING_EXPRESSION = '上个还没好，爬去排队' #处理消息时其他命令的回复
# 设置过期超时为 1 分钟，即用户 1 分钟不发消息后，会话将被关闭
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=1)
```

## 教程

### go-cqhttp启动与配置
https://docs.go-cqhttp.org/guide/#go-cqhttp
在官网上下载go-cqhttp Windows版
#### Windows 标准方法

1.  双击`go-cqhttp.exe`此时将提示

```
[WARNING]: 尝试加载配置文件 config.hjson 失败: 文件不存在
[INFO]: 默认配置文件已生成,请编辑 config.hjson 后重启程序.
```
2.   编辑新生成的config.hjson填入参数
 ```
// QQ号
uin: xxxxxxxxx
 // QQ密码
password: "xxxxxxxxx"
// 反向WS设置 =>修改该项配置
// 是否启用该推送
            enabled: true
            reverse_url: "ws://127.0.0.1:8080/ws/"
            //此项 应与配置_2的ip与端口相同，若docker注意docker网络的ip
```
3.  再次双击`go-cqhttp.exe`
首次登录需要认证的信息, 请自行认证设备方式参考以下链接。
https://docs.go-cqhttp.org/faq/slider.html#%E6%96%B9%E6%A1%88a-%E8%87%AA%E8%A1%8C%E6%8A%93%E5%8C%85

4.  再次双击`go-cqhttp.exe`
保持该exe的运行状态
```
[INFO]: 登录成功 欢迎使用: balabala
```

### yryd_bot启动与配置
1. python3环境搭建（略）
2. 安装依赖（yryd_bot文件夹下cmd命令）
```
 pip install -r requirements.txt
```
4. 配置文件的写入（配置_1,配置_2）
配置_1key申请地址：
- https://dev.qweather.com/docs/api/weather/weather-now/ 和风天气
- https://api.lolicon.app/#/setu 色图api
5. 选择是否添加附加功能
附加功能为：p站标签搜图、p站pid下载图片、循环翻译
在add文件夹中复制xxxx_api.py文件放入api文件夹，复制xxx.py文件放入yryd_bot\yryd_cmd\plugins
附加功能key填入xxx.py文件中：
- https://fanyi-api.baidu.com/api/trans/product/desktop?req=developer 百度翻译api
- https://pypi.org/project/PixivPy/ P站图片获取包（refresh_token）参考下链接
- https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362
6. 运行 bot.py开启你的QQ机器人
7. nonebotF&Q使用文档 https://docs.nonebot.dev/guide/
