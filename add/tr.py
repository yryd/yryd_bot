from nonebot import on_command, CommandSession
from api.bdtrans_api import *

@on_command('tr', aliases=('长翻译'), only_to_me=True)
async def translate(session: CommandSession):
    type = session.get('type', prompt='目的语种~？')
    if type == "e":
        type = "en"
    elif type == "j":
        type = "jp"
    else:
        type = "zh"
    trans_content = session.get('con', prompt='查☆什☆么☆词？')
    if trans_content != 'xxx':
        mes = session.event.raw_message
        if mes != 'xxx':
            translate_report = bdtrans(mes, "auto", type)
            await session.send(translate_report)
            await session.send('查☆什☆么☆词？')
        if mes == 'xxx':
            session.state['con'] = 'xxx'
            await session.send('任意输入退出~')
        # print(session.state)
        session.pause()

    await session.send('已☆结☆束☆翻☆译~')
