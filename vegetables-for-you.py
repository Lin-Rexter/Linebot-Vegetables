# coding=utf-8
import datetime
import random
from LineBotApi import line_reply, line_reply_run
from WebSpider import Vegetables_info_parse
#from PostgreSQL import pg_config


# 爬蟲
def Spider(Spider_name):
    # Spider_name: 爬蟲模組
    Spider = Spider_name

    New_url = Spider['urls'] # 爬取最新蔬菜行情

    try:
        return New_url # 發送最新蔬菜行情至Line
    except Exception as e:
        print(e)


def reply():
    Vegetables_Spider = Spider(Vegetables_info_parse)
    line_reply(spider_name=Vegetables_Spider)


if __name__ == "__main__":
    line_reply_run()
    reply()