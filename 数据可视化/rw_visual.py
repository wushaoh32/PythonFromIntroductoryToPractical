import  matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #创建一个Random实例
    rw = RandomWalk()
    rw.fill_walk()

    #将所有的点绘制出来
    plt.style.use('classic')
    #在matplotlib库中，subplots是一个用来创建包含多个子图的图形对象的函数，方便用户在一个图形界面同时绘制多个不同的图表
    fig,ax = plt.subplots()
    #列表长度
    point_numbers = range(rw.num_points)
    #浅蓝到深蓝的颜色映射,edgecolors='none'是删除点的轮廓
    ax.scatter(rw.x_values,rw.y_values,c = point_numbers
               ,cmap= plt.cm.Blues,
               edgecolors= 'none',s = 15)
    # #scatter是绘制散点图的函数
    # ax.scatter(rw.x_values,rw.y_values,s = 15)
    #指定两条轴上刻度的间距必须相等“方向”
    ax.set_aspect('equal')

    #突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #绘制柱形条
    #plt.colorbar()
    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break


