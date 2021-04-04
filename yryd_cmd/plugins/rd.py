from nonebot import on_command, CommandSession
from api.random_api import *

@on_command('rd', aliases=('rd', '骰子'), only_to_me=False)
async def rd(session: CommandSession):
    #去除所有空格
    stripped_arg = session.current_arg_text.strip()
    session.state['num_scr'] = stripped_arg
    num_scr = session.get('num_scr')
    person = session.event.sender['nickname']
    nd = 1
    #参数情况支持三种输入，默认为空、数字、xdx
    if not num_scr:
        true_num_scr = '100'
    if num_scr.isdigit():
        true_num_scr = num_scr
    if num_scr.find('d') != -1:
        nd, true_num_scr = num_scr.split('d')

    rd_report = await get_rd(nd, true_num_scr, person)
    await session.send(rd_report)

async def get_rd(nd, num_scr_str, person):
    num_scr_len = int(num_scr_str) * int(nd)
    num_scr_suf = random_n1dn2(int(nd), int(num_scr_str))
    return f'{person} 掷骰{nd}d{num_scr_str} ：{num_scr_suf}/{num_scr_len}'
