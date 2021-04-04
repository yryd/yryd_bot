from nonebot import on_command, CommandSession
from api.translate_api import *

@on_command('translate', aliases=('翻译', 'translate', 'trans'), only_to_me=False)
async def translate(session: CommandSession):
    trans_content = session.get('trans_content', prompt='诶多……查☆什☆么☆词？')
    translate_report = fanyi(trans_content)
    await session.send(translate_report)
    all = f'「{trans_content}」=>>' + translate_report
    await session.send(all)

# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@translate.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['trans_content'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('爬，输入不能为空')
    session.state[session.current_key] = stripped_arg
