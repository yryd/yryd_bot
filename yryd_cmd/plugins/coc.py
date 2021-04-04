from nonebot import on_command, CommandSession
from api.random_api import *

@on_command('coc', aliases=('coc', 'coc车卡', 'coc做成'), only_to_me=False)
async def ldst(session: CommandSession):
    person = session.event.sender['nickname']
    ldst_report = await get_ldst(person)
    await session.send(ldst_report)

async def get_ldst(person):
    #力量
    STR = random_n1dn2(3,6)*5
    #体质
    CON = random_n1dn2(3,6)*5
    #体型
    SIZ = random_n1dn2(2,6)*5
    #敏捷
    DEX = random_n1dn2(3,6)*5
    #外貌
    APP = random_n1dn2(3,6)*5
    #智力
    INT = random_n1dn2(2,6)*5
    #意志
    POW = random_n1dn2(3,6)*5
    #教育
    EDU = random_n1dn2(2,6)*5
    #幸运
    LUK = random_n1dn2(3,6)*5

    SUM = STR + CON + SIZ + DEX + APP + INT + POW + EDU + LUK
    return f'{person}的调查员做成：\n力量：{STR}体质：{CON}体型：{SIZ}敏捷：{DEX}外貌：{APP}智力：{INT}意志：{POW}教育：{EDU}幸运：{LUK}共计：{SUM}/560'

# coc规则
# 如果你选择了骰点法，那么请记住3个属性：体型、智力、教育。除了这3个的决定方式是2D6+6，其他属性的决定方式都是3D6。
