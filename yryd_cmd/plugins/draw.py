from nonebot import on_command, CommandSession
from api.draw_api import *
import random


"""随机从四个卡池选一个，再平均抽卡"""
def draw_card(rank_4,rank_3,rank_2,rank_1):
    point = random.randint(0, 99)
    finally_result = ''
    rank = 0
    if 0 <= point < 3:
        finally_result = rank_4[random.randint(0, len(rank_4) - 1)]
        rank = '★★★★'
    if 3 <= point < 18:
        finally_result = rank_3[random.randint(0, len(rank_3) - 1)]
        rank = '★★★☆'
    if 18 <= point < 88:
        finally_result = rank_2[random.randint(0, len(rank_2) - 1)]
        rank = '★★☆☆'
    if 88 <= point < 100:
        finally_result = rank_1[random.randint(0, len(rank_1) - 1)]
        rank = '★☆☆☆'
    return finally_result, rank

@on_command('draw', aliases=('dr', '抽卡'), only_to_me=False)
async def rd(session: CommandSession):
    #去除所有空格
    stripped_arg = session.current_arg_text.strip()
    session.state['num_scr'] = stripped_arg
    num_scr = session.get('num_scr')
    person = session.event.sender['nickname']
    flag = 0
    #参数情况
    if not num_scr:
        true_num_scr = '10'
    if num_scr.isdigit():
        true_num_scr = num_scr
    if num_scr.find('ssr') != -1:
        true_num_scr = '1'
        flag = 1
    # 获取
    rd_report = await get_rd(flag, int(true_num_scr), person)
    # 向用户发送帮助
    await session.send(rd_report)

async def get_rd(flag, num_scr_str, person):
    #该函数仅字符串返回值
    # a <= n <= b
    loop = int(num_scr_str)
    rank_4,rank_3,rank_2,rank_1 = request_draw()
    str = ''
    if flag == 1:
        char = rank_4[random.randint(0, len(rank_4) - 1)]
        send = f'{person}单抽一张金卡:\n★★★★{char}'
        return send
    for i in range(num_scr_str):
        char, color = draw_card(rank_4,rank_3,rank_2,rank_1)
        str = f'{color}{char}\n' + str
    return f'{person}抽取{num_scr_str}次:\n' + str + '抽取完毕~'
