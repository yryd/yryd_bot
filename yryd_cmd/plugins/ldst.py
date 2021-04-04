from nonebot import on_command, CommandSession
from api.ldst_api import *

@on_command('ldst', aliases=('lsdt', '色图', '来点色图'), only_to_me=False)
async def ldst(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    session.state['r18'] = stripped_arg
    # 判断用户是否输入1，输入则打开r18开关
    r18 = session.get('r18')
    if not r18:
        r18 = '0'
    ldst_report = await get_ldst(r18)
    await session.send(ldst_report)

@ldst.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['r18'] = stripped_arg
        return
    session.state[session.current_key] = stripped_arg


async def get_ldst(r18):
    if r18 == 'h':
        r18 = 1
    else:
        r18 = 0
    arr_setu = setu_api(r18)
    return f'[CQ:image,file={arr_setu[0]}]' + f'\n作者：{arr_setu[2]}\n标题：{arr_setu[1]}\nuid：{arr_setu[3]}\npid:{arr_setu[4]}'
