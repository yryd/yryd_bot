from nonebot import on_command, CommandSession
from api.pixiv_api import *

@on_command('pstag', aliases=('标签搜图'), only_to_me = True)
async def card(session: CommandSession):
    para = session.get('para', prompt='吾辈不明白啊——？参数呢？')
    """参数形式为tag x page x show，分割参数"""
    p4 = 0
    p1, p2, p3 = para.partition('x')
    if p3.find('x') != -1:
        p2, p3, p4 = p3.partition('x')
        p3 = p2
    # print(p1, p3, p4)
    card_report = await get_search(p1, p3, p4)
    await session.send(card_report)


@card.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['para'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('爬，输入不能为空')
    session.state[session.current_key] = stripped_arg


async def get_search(p1, p3, p4):
    result = search_img(p1, p3, p4)
    return result
