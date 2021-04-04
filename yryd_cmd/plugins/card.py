from nonebot import on_command, CommandSession
from api.card_api import *

@on_command('card', aliases=('双生卡牌', '立绘', '卡牌'), only_to_me=False)
async def card(session: CommandSession):
    try:
        char_0 = session.get('char', prompt='诶多……查哪个「少女服装」の立绘呢？')
        char_1, char_2 = char_0.split('x')
        char = char_1 + '·' + char_2
        card_report = await get_card_of_char(char)
        await session.send(card_report)
    except:
        await session.send("输入格式参考.card 服装x少女")
@card.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['char'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('爬，输入不能为空')
    session.state[session.current_key] = stripped_arg


async def get_card_of_char(char: str) -> str:
    name, src = request_sssj_card(char)
    name_0, type = name.split('.')
    return f'[CQ:image,file={src}]\n' + f'{name_0}'
