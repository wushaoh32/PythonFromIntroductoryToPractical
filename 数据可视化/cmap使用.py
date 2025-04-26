import matplotlib.pyplot as plt
import numpy as np

# 生成数据
x = np.random.randn(50)
y = np.random.randn(50)
z = np.random.rand(50)  # 用于颜色映射的数据

# 绘制散点图，使用plot.cm.Blues颜色映射
plt.scatter(x, y, c=z, cmap=plt.cm.Blues)
plt.colorbar()  # 添加颜色条，用于显示颜色映射与数据值的对应关系

plt.show()