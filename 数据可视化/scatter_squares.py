import matplotlib.pyplot as plt

x_values = range(-1001,1001)
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')

fig,ax = plt.subplots()
#ax.scatter(x_values,y_values,color='red',s=10)#s在这里是指线条的粗细
ax.scatter(x_values,y_values,c = y_values,cmap = plt.cm.Blues ,s=10)#s在这里是指线条的粗细
ax.set_title("Square Numbers",fontsize=24)
ax.set_xlabel("Value",fontsize=14)
ax.set_ylabel("Square of Value",fontsize=14 )
#标记刻度样式稠密
ax.tick_params(labelsize=10)
#设置每个坐标轴的取值范围,你可以指定，但你别瞎指定
ax.axis([-1001, 1001,-1_000_000_000,1_000_000_000])
#刻度标签样式
ax.ticklabel_format(style = 'sci')#sci值科学计数法
#plt.show()
plt.savefig('squares2.png',bbox_inches='tight')#第二个参数是裁白边的