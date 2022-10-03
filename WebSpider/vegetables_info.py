import requests
import json
from pprint import pprint
from bs4 import BeautifulSoup
from .user_agent import UA
from urllib.parse import urljoin # 解析相對網址


# 新增字典
def dict_add(name, key, values):
    name.setdefault(key, []).append(values) # 使用setdefault優點，自動新增預設值


# 爬取最新蔬菜行情
def Vegetables_info_parse():
    r = requests.get(
            'https://',
            headers={
                "User-Agent": UA
            }
        )

    soup = BeautifulSoup(r.text, 'lxml') # 使用lxml解析效率高
    article = soup.select("")

    # 設置爬取資訊方式
    def List(ver):
        meta = {
                'url':urljoin('https://', ver.select_one('')[''])
            }
        return meta

    # 放置所有資訊
    All = {} 
    for x in article:
        dict_add(All, '', List(x)[''])

    return All