#中文分词
import jieba
#读文件
with open('laptops.csv','r',encoding='utf-16') as file:
    s = file.read()
#print(s)
#分词
lst = jieba.lcut(s)
#print(lst)

#使用集合操作进行去重
set1 = set(lst)
#使用字典统计出现的值的频率，key作为词，value作为出现的次数
d={}
for  item in set1:
    if len(item) >= 2:
        d[item]=0
print(d)

for item in lst:
    if item in d:
        d[item] = d.get(item)+1
#print(d)
new_list = []
for item in d:
    new_list.append([item,d[item]])
print(new_list)
#列表排序
#.sort是直接排
#sorted是返回一个新列表
new_list.sort(key = lambda x:x[1],reverse=True)
print(new_list[0:11])