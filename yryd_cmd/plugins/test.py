from nonebot import on_command, CommandSession

@on_command('test', aliases=('test', '测试'))
async def test(session: CommandSession):
    #去除所有空格
    stripped_arg = session.current_arg_text.strip()
    session.state['temp'] = stripped_arg
    # print(session.event.sender)
    # {'age': 0, 'nickname': '昵称', 'sex': 'unknown', 'user_id': 26466xxxxxxx}
    temp = session.get('temp')
    # 无参数情况
    if not temp:
        temp = '0' + session.event.sender['nickname']
    # 输出参数处理结果
    await session.send(temp)
