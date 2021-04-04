from nonebot import on_command, CommandSession
from api.img_api import *

@on_command('img', aliases=('image', '来图'), only_to_me=False)
async def img(session: CommandSession):
    num = session.get('num', prompt='选择一个「次の元」:1-6')
    img_url= star_num(num)
    img_report = f'[CQ:image,file={img_url}]'
    await session.send(img_report)

@img.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['num'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('爬，输入不能为空')
    session.state[session.current_key] = stripped_arg
