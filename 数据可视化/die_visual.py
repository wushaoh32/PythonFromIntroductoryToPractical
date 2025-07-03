from die import Die
import plotly.express as px
#创建一个D6
die = Die()
#掷骰子的结果
results = []
for roll_num in range(1000):
    #调用die对象的roll方法，将结果赋值给变量result
    result = die.roll()
    results.append(result)
#分析结果
#空列表，用于存储每个点出现的次数
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#对数据进行可视化
#定义图题
title = "Results of Rolling one D6 1,000 Timer"
labels = {'x':'Result','y':'Frequency'}
fig = px.bar(x=poss_results, y=frequencies,title =  title,labels = labels)
fig.show()
