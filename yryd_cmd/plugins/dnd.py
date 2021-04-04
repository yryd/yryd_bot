from nonebot import on_command, CommandSession
from api.random_api import *

@on_command('dnd', aliases=('dnd', 'dnd车卡', 'dnd做成'), only_to_me=False)
async def ldst(session: CommandSession):
    person = session.event.sender['nickname']
    ldst_report = await get_ldst(person)
    await session.send(ldst_report)

async def get_ldst(person):
    #力量
    STR = random_maxn_nd6(3,4)
    #体质
    CON = random_maxn_nd6(3,4)
    #敏捷
    DEX = random_maxn_nd6(3,4)
    #智力
    INT = random_maxn_nd6(3,4)
    #感知
    FEL = random_maxn_nd6(3,4)
    #魅力
    APP = random_maxn_nd6(3,4)

    SUM = STR + CON + DEX + INT + FEL + APP
    return f'{person}的英雄做成：\n力量：{STR}体质：{CON}敏捷：{DEX}智力：{INT}感知：{FEL}外貌：{APP}共计：{SUM}'
