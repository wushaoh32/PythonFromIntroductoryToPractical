#choice是python标准库random模块中的函数，它的作用是从非空序列中随机选取一个元素
from random import choice
class RandomWalk:
    """生成一个随机游走的类"""
    def __init__(self, num_points = 500):
        """初始化随机游走的属性"""
        #self代表类的实例本身。self.num_points是在定义一个属于类实例的属性，这里把形参的值赋给实例属性
        #方法和属性无对应关系，但一个方法涉及多个属性
        self.num_points = num_points
        #所有随机游走始于（0,0）
        self.x_values = [0]#将列表[0]赋值给实例属性
        self.y_values = [0]

    def fill_walk(self):
        """计算随机游走经过的所有点"""

        #不断游走，直到列表到达指定长度
        while len(self.x_values) < self.num_points:
            #while循环中，条件为true，执行循环语句
            #决定前进的方向以及演这个方向前进的距离
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #拒绝原地踏步
            if x_step ==0 and y_step ==0:
                continue #此处continue是跳出当前循环中的剩余代码直接进入下一次的while循环迭代

            #计算下一个点的x坐标值和y坐标值
            x = self.x_values[-1] + x_step #x_values的意思是列表的最后一个值
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
