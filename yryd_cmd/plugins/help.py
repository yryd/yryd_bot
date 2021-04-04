from nonebot import on_command, CommandSession


@on_command('help', aliases=('help', '帮助'), only_to_me=False)
async def help(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    session.state['help_content'] = stripped_arg
    help_con = session.get('help_content')
    # print(help_con)
    # print(help_con.find('yryd') != -1)
    #参数情况:获取哪部分的帮助
    if help_con.find('跑团') != -1:
        help_str = help_part_1()
    elif help_con.find('图片') != -1:
        help_str = help_part_2()
    elif help_con.find('杂类') != -1:
        help_str = help_part_3()
    elif help_con.find('双生') != -1:
        help_str = help_part_4()
    elif help_con.find('yryd') != -1:
        help_str = help_part_hidden()
    else:
        help_str = help_part_0()

    await session.send(help_str)

def help_part_1():
    wel_str = '跑团类使用帮助：\n------------\n'
    fun_1 = '1.coc人物做成\n命令：.coc\n'
    fun_2 = '2.dnd人物做成\n命令：.dnd\n'
    fun_3 = '3.掷骰子\n示例命令：.rd 4d6\n参数不写默认为1d100\n也支持参数为纯数字\n'
    help_str = wel_str + fun_1 + fun_2 + fun_3
    return help_str

def help_part_2():
    wel_str = '图片类使用帮助：\n------------\n'
    fun_1 = '1.随机图片\n示例命令：.img 6\n参数为图库1-6\n其中2为mc酱图集\n'
    fun_2 = '2.随机色图\n命令：.ldst\n「显然是不够色的」\n'
    fun_3 = '3.p站标签搜图(限私聊)\n示例命令：.pstag 水着x2\n参数为tagxpage|1页显示30个\n「用太多了会宕机」\n(仅源码支持)\n'
    help_str = wel_str + fun_1 + fun_2 + fun_3
    return help_str

def help_part_3():
    wel_str = '杂类使用帮助：\n------------\n'
    fun_1 = '1.世界天气\n示例命令：.天气 伊拉克\n参数为城市\n'
    fun_2 = '2.中英互译\n示例命令：.翻译 雨季\n参数为翻译内容\n'
    fun_3 = '3.今日人品\n示例命令：.jrrp\n「相信的人不会多测」\n'
    fun_4 = '4.知乎日报\n示例命令：.zhihu\n「没什么用」\n'
    fun_5 = '5.渣语\n示例命令：.zy\n「如果你想听点好听的」\n'
    fun_6 = '6.随机笑话\n示例命令：.joke\n「过时的没品笑话」\n'
    help_str = wel_str + fun_1 + fun_2 + fun_3 + fun_4 + fun_5 + fun_6
    return help_str

def help_part_4():
    wel_str = '双生视界使用帮助：\n------------\n'
    fun_1 = '1.获取卡面\n示例命令：.card 水着x艾琳\n参数为服装x少女\n'
    fun_2 = '2.普池抽卡\n示例命令：.dr 20\n参数为数字默认10\n'
    fun_3 = '3.普池武器\n示例命令：.dw 20\n参数为数字默认10\n'
    help_str = wel_str + fun_1 + fun_2 + fun_3
    return help_str

def help_part_hidden():
    wel_str = '隐藏空间：\n------------\n(仅源码支持)\n'
    fun_1 = '1.色图r18\n命令：.ldst h\n'
    fun_2 = '2.pid发图\n示例命令：.pidi 84782392\n'
    fun_3 = '3.循环翻译\n示例命令：.tr\n目标语言e英语j日语其他中文\n输入xxx结束\n'
    help_str = wel_str + fun_1 + fun_2 + fun_3
    return help_str

def help_part_0():
    wel_str = '「二·次·元」酱V2.0\n使用帮助：\n------------\n命令以「!」「／」「.」「。」开头\n注意命令的空格\n------------\n'
    fun_1 = '1.跑团类\n（包括简易车卡、掷骰子）\n参考命令：.help 跑团\n'
    fun_2 = '2.图片类\n（包括随机图片、壁纸）\n参考命令：.help 图片\n'
    fun_3 = '3.杂类\n（包括翻译、今日人品等）\n参考命令：.help 杂类\n'
    fun_4 = '4.双生视界\n（包括抽卡、抽武器、卡面获取）\n参考命令：.help 双生\n'
    fun_5 = '5.隐藏命令\n参考命令：无\n「藏在了不会得到的地方」\n'
    help_str = wel_str + fun_1 + fun_2 + fun_3 + fun_4 + fun_5
    return help_str
