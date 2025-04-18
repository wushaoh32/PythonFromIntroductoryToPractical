import requests#HTTP请求响应库
import re#正则表达式库

url = 'https://www.weather.com.cn/'
resp = requests.get(url)#模块对象使用函数方法指向url

#直接输出的话，显示的是一个网页的html和一些乱码，所以我需要设置一下编码格式
resp.encoding = 'utf-8'#在函数调用时使用括号，在设置配置和赋值时用等号

#print(resp.text)#对象名.属性名（属性是对象所具有的特性）

#findall用于在字符串中查找所有符合正则表达式模式的子串，并以列表的形式返回
#(要匹配的正则表达式模式,要在其中进行查找的字符串)
city = re.findall('title="([\u4e00-\u9fff]*)"',resp.text)
lst = []
for item in city:
    lst.append(item)
    print(item)