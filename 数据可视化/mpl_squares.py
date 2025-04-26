import  matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示异常

input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_value,squares,linewidth=3)

#设置图标标题，并给坐标轴加上标签
ax.set_title("平方数",fontsize=14)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)
#设置标记刻度的大小
ax.tick_params(axis='both', labelsize=14)

ax.plot(squares)

plt.show()