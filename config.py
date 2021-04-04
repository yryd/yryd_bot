from nonebot.default_config import *
from datetime import timedelta

SUPERUSERS = {264xxxxxx} #填写本人QQ
COMMAND_START = {'/', '!', '／', '！', '.', '。'}
HOST = '127.0.0.1'
PORT = 8080
NICKNAME = {'阿sir', '啊sir'}
SESSION_RUNNING_EXPRESSION = '上个还没好，爬去排队'
# 设置过期超时为 1 分钟，即用户 1 分钟不发消息后，会话将被关闭
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=1)
