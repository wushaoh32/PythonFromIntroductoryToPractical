import pandas as pd
import matplotlib.pyplot as plt
#读取Excel文件
df = pd.read_excel('备件导入模版.xlsx')
print(df)
#解决在使用绘图时的中文乱码问题
plt.rcParams['font.sans-serif'] = ['Simhei']
#设置画布的大小
plt.figure(figsize=(10,6))
lables = df['物料名称']
y = df['价格']
print(lables)
print(y)

#绘制饼图
plt.pie(y,labels=lables,autopct='%1.1f%%',startangle=90)
#设置x,y轴刻度
plt.axis('equal')
plt.title('汽车价格')
plt.show()