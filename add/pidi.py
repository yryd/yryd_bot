from nonebot import on_command, CommandSession
from aiocqhttp.message import MessageSegment
from api.pixiv_api import *

@on_command('pidi', aliases=('id搜图'), only_to_me = True)
async def card(session: CommandSession):
    id = session.get('id', prompt='吾辈不明白啊——？参数呢？')
    url_0 = pid_get_img(id)
    bot = session.bot
    headers_0=[
    "User-Agent=Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Referer=https://www.pixiv.net/"
    ]
    re = await bot.download_file(url=url_0, thread_count=3, headers=headers_0)
    file = re['file']
    c1, c2, c3 = file.partition('cache')
    c3 = c3[1:]
    await session.send(MessageSegment.image("{}".format(f'../cache/{c3}')))


@card.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['id'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('爬，输入不能为空')
    session.state[session.current_key] = stripped_arg
