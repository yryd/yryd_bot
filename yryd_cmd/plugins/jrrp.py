from nonebot import on_command, CommandSession
from api.random_api import *

@on_command('jrrp', aliases=('jrrp', '今日人品', '每日人品'), only_to_me=False)
async def jrrp(session: CommandSession):
    person = session.event.sender['nickname']
    jrrp_report = await get_jrrp(person)
    await session.send(jrrp_report)

async def get_jrrp(person):
    jp = random_n1dn2(1, 100)
    if 1 <= jp <= 20:
        star = '★☆☆☆☆'
    if 20 <= jp <= 40:
        star = '★★☆☆☆'
    if 40 <= jp <= 60:
        star = '★★★☆☆'
    if 60 <= jp <= 80:
        star = '★★★★☆'
    if 80 <= jp <= 100:
        star = '★★★★★'
    return f'今日运势：{star}\n「{person}」今天的好运超过%{jp}的人'
