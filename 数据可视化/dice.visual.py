import plotly.express as px
from die import Die
from 数据可视化.die_visual import poss_results

#创建两个D6
die_1 = Die()
die_2 = Die()

#投骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    #调用die对象的roll方法
    result = die_1.roll()+die_2.roll()
    #此处results里面存了1000个和
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
#此时的poss_results是一个range对象，是一个序列，不是列表
poss_results = range(2,max_result+1)
for value in poss_results:
    #遍历poss_results中的每个“可能和”（2,3，...,12）
    #count(3)就是统计列表中值为3的个数元素
    frequency = results.count(value)
    frequencies.append(frequency)
#可视化结果
title = "Results of Rolling Two D6 Dice 1,000 Timer"
labels = {'x':'Result','y':'Frequency of result'}
fig = px.bar(x=poss_results,y=frequencies,title = title,labels = labels)
fig.show()
