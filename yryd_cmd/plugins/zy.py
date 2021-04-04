import requests
from nonebot import on_command, CommandSession

# 来源https://github.com/fz6m/nonebot-plugin
@on_command('zy', aliases=('渣语'), only_to_me=False)
async def lovelive(session: CommandSession):
    lovelive_send = await get_lovelive()
    await session.send(lovelive_send, at_sender=True)


async def get_lovelive():
    url = 'https://api.lovelive.tools/api/SweetNothings'
    return requests.get(url).text
