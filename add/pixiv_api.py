from pixivpy3 import *
import time

# 具体token获取访问pixivpy的pip官网
TOKEN = ''
aapi = AppPixivAPI()
aapi.auth(refresh_token = TOKEN)
"""标签搜索"""
def search_img(key_tag, page, show = 0):
    page = int(page) - 1
    show = int(show) - 1
    # key_tag = '水着'
    json_result = aapi.search_illust(key_tag, search_target='partial_match_for_tags')
    illust_list = json_result.illusts
    # 每页30个，下一页
    for n in range(page):
        time.sleep(0.5)
        next_qs = aapi.parse_qs(json_result.next_url)
        json_result = aapi.search_illust(**next_qs)
        next_illust = json_result.illusts
        illust_list = next_illust
    str_result = []
    p_img_list = []
    str_result_long = ''
    id_in_page = 0
    for i in illust_list:
        id_in_page = id_in_page + 1
        p_title = i.title
        p_img = i.image_urls['large']
        p_img_list.append(p_img)
        pid = i['id']
        user_dict = i['user']
        uid = user_dict['id']
        author = user_dict['name']
        str =  f'{id_in_page}.{p_title}\npid：{pid}\nuid：{uid}\nauthor：{author}\n'
        str_result.append(str)
        str_result_long = str_result_long + str
    sum_str = f'本页为第{page + 1}页\n' + str_result_long
    single_str = str_result[show]
    if show <= -1:
        return sum_str
    elif show > 30:
        return '哔哔~数据溢出¿数据要求30条以下'
    else:
        return single_str

def pid_get_img(pid):
    json_result = aapi.illust_detail(int(pid))
    illust = json_result.illust
    return illust.image_urls['large']

if __name__=='__main__':
    """标签、第几页、第几条（默认0全输出）"""
    a = search_img('gosick', 2, 24)
    print(a)
    b = pid_get_img(84782392)
    print(b)
