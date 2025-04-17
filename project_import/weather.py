import requests
import re

#定义打包函数
def get_html():
    url = 'https://www.weather.com.cn/'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    return resp.text

#定义解析函数
def parse_html(html_str):
    city = re.findall('title="([\u4e00-\u9fff]*)"',html_str)
    lst=[]
    for item in city:
        lst.append(item)
    return lst